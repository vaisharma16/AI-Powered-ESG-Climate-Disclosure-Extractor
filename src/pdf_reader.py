import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        full_text += f"\n--- Page {page_num + 1} ---\n{text}"

    return full_text

def save_text_file(text, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

def process_all_pdfs(input_folder="data/raw", output_folder="data/processed"):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace(".pdf", ".txt"))
            print(f"Extracting text from: {filename}")
            text = extract_text_from_pdf(input_path)
            save_text_file(text, output_path)
            print(f"Saved to: {output_path}")

if __name__ == "__main__":
    process_all_pdfs()
