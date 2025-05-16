# src/qa_with_gemini.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add project root

import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

from src.config import CLIMATE_DISCLOSURE_QUESTIONS
from src.postprocessor import postprocess_all
from src.vector_store import load_vector_store

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

import re
import json

def ask_gemini_with_context(db, question):
    results = db.similarity_search(question, k=4)
    combined_context = "\n\n".join([r.page_content for r in results])

    prompt = f"""
    You are an expert ESG analyst. Given the following CONTEXT, extract an accurate answer to the QUESTION using specific, factual details. Answer should be concise and cite relevant emissions, targets, governance actions, or climate scenarios.

    CONTEXT:
    ```text
    {combined_context}
     QUESTION:
    {question}

    Return your response as a JSON:
    {{
    "answer": "...",
     "confidence_score": 0.0 - 1.0,
    "page_reference": "page X, page Y"
    }}
    """
    try:
        response = model.generate_content(prompt)
        match = re.search(r"{.*}", response.text, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            return {
                "answer": "Could not parse",
                "confidence_score": 0,
                "page_reference": "N/A"
     }
    except Exception as e:
        return {
"answer": f"Error: {str(e)}",
"confidence_score": 0,
"page_reference": "N/A"
}

def extract_with_retrieval(question, db, top_k=4):
    results = db.similarity_search(question, k=top_k)
    
    for r in results:
        print(f"Page {r.metadata.get('page_number')}: {r.page_content[:300]}")
    combined_context = "\n---\n".join([f"(Page {r.metadata.get('page_number')})\n{r.page_content}" for r in results])
    return ask_gemini_with_context(question, combined_context)

def run_full_qa(output_path="outputs/vector_output.json"):
    db = load_vector_store()
    qa_result = {}

    for question in CLIMATE_DISCLOSURE_QUESTIONS:
        print(f"🔍 Asking: {question}")
        raw = extract_with_retrieval(question, db)

        try:
            match = re.search(r"\{.*\}", raw, re.DOTALL)
            qa_result[question] = json.loads(match.group()) if match else {"answer": raw, "confidence_score": 0, "page_reference": "N/A"}
        except:
            qa_result[question] = {"answer": raw or "Not found", "confidence_score": 0, "page_reference": "N/A"}

    # Clean it
    final_result = postprocess_all(qa_result)
    os.makedirs("outputs", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_result, f, indent=2)
    print(f"✅ Results saved to {output_path}")

if __name__ == "__main__":
    run_full_qa()
