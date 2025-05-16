# src/app.py
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add project root

import streamlit as st
import tempfile
import os
from src.vector_store import pdf_to_documents, build_vector_store, save_vector_store, load_vector_store
from src.qa_with_gemini import ask_gemini_with_context
from src.config import CLIMATE_DISCLOSURE_QUESTIONS

st.set_page_config(page_title="AI-Powered ESG & Climate Disclosure Extractor", layout="wide")
st.title("🌍 AI-Powered ESG & Climate Disclosure Extractor")
st.caption("Built with Gemini + LangChain | Aligned with TCFD/CDP")

uploaded_file = st.file_uploader("Upload ESG/Climate PDF Report", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    st.success("✅ PDF uploaded successfully")

    with st.spinner("📚 Extracting text and building vector store..."):
        docs = pdf_to_documents(pdf_path)
        db = build_vector_store(docs)

    st.success("✅ Vector store created. Ready for question answering.")

    st.subheader("📊 Extracted Climate Disclosures")

    results = {}
    for question in CLIMATE_DISCLOSURE_QUESTIONS:
        with st.spinner(f"🔍 {question}"):
            response = ask_gemini_with_context(db, question)
            results[question] = response

            st.markdown(f"### ❓ {question}")
            st.write("**Answer:**", response.get("answer"))
            st.write("**Confidence:**", response.get("confidence_score"))
            st.write("**Page Reference:**", response.get("page_reference"))

    st.success("✅ Extraction complete")
