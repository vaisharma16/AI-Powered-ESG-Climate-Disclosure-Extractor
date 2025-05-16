# src/vector_store.py

import os
import fitz  # PyMuPDF
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


def pdf_to_documents(pdf_path):
    """Extracts text by page and returns list of LangChain Documents with metadata."""
    doc = fitz.open(pdf_path)
    documents = []
    for i, page in enumerate(doc):
        text = page.get_text()
        if text.strip():
            documents.append(Document(
                page_content=text,
                metadata={"page_number": i + 1, "source": os.path.basename(pdf_path)}
            ))
    return documents


def build_vector_store(documents):
    """Splits documents into chunks, creates embeddings, and stores them in FAISS."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    db = FAISS.from_documents(chunks, embedding=embeddings)
    return db


def save_vector_store(db, save_dir="vector_index"):
    db.save_local(save_dir)


def load_vector_store(load_dir="vector_index"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return FAISS.load_local(load_dir, embeddings, allow_dangerous_deserialization=True)
