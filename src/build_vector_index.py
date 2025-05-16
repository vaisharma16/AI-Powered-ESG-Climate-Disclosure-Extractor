import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add project root

from src.vector_store import pdf_to_documents, build_vector_store, save_vector_store

def main(pdf_path):
    print(f"Loading PDF and extracting documents from {pdf_path}...")
    docs = pdf_to_documents(pdf_path)
    print(docs[0].page_content[:500])
    
    print(f"Building FAISS vector store from {len(docs)} documents...")
    db = build_vector_store(docs)

    print("Saving vector store locally...")
    save_vector_store(db)

    print("✅ Vector index built and saved to 'vector_index/'")

if __name__ == "__main__":
    # Change this to your actual PDF path
    main("data/processed/unilever-climate-transition-action-plan-updated-2024.txt")
