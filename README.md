# 🌍 AI-Powered ESG & Climate Disclosure Extractor

*LangChain + Gemini Pro + FAISS + Streamlit*  
Extract ESG & Climate Intelligence from Sustainability PDFs – Aligned with TCFD/CDP

---

## 📌 Overview

This GenAI-powered tool automates the extraction of ESG (Environmental, Social, Governance) and climate-related disclosures from complex, multi-column PDF sustainability reports.  
It uses Google Gemini Pro in combination with LangChain, FAISS, and Streamlit to perform retrieval-augmented question answering on unstructured ESG data.

Designed for ESG analysts, data scientists, and sustainability teams, this app aligns with industry frameworks such as **TCFD** (Task Force on Climate-related Financial Disclosures) and **CDP**.

---

## ✅ Core Features

- 🔍 **Extract Scope 1, 2, and 3 GHG emissions**
- 🎯 **Identify net-zero targets, climate risk disclosures, and ESG governance structures**
- 💡 **Ask contextual questions directly to uploaded ESG/Climate PDFs**
- 🧠 **Uses LangChain + Gemini Pro for intelligent Q&A**
- 📚 **Context retrieved using FAISS vector search**
- 🖥️ **Clean, interactive Streamlit UI**

---

## 🚀 Tech Stack

| Layer         | Tool/Library                       |
|---------------|------------------------------------|
| 💬 LLM        | Google Gemini Pro (`google.generativeai`) |
| 📚 Retrieval  | FAISS (via `langchain_community`)  |
| 📄 PDF Parsing| PyMuPDF (`fitz`)                   |
| 🧱 Framework  | LangChain, LangChain-Google-GenAI  |
| 🌐 Frontend   | Streamlit                          |
| 🔐 Env Mgmt   | python-dotenv                      |

---

## 🧠 What It Can Do

Upload any ESG or climate-related PDF report (e.g., Infosys, Unilever, Wipro), and:

- Build a semantic vector index from the PDF
- Ask domain-specific questions such as:
    - “What are the company’s Scope 3 emissions?”
    - “Is there a board-level ESG committee?”
    - “Does the company mention climate scenario analysis?”
- Get answers with page references and confidence scores
- Export the results as JSON for integration into ESG pipelines

---

## 🖼️ UI Snapshot (Flow)
- ✅ Upload: Unilever_Sustainability_Report.pdf
- ✅ Vector Index Created (FAISS)
- ✅ Ask: "What are Scope 1 emissions?"
- 📤 Output: "6,515 tCO2e in 2023... (Page 42, Confidence: 0.95)"


---

## 📁 Project Structure
```

ai-esg-disclosure-extractor/
├── app/ # Streamlit UI code
├── data/ # Raw PDFs and preprocessed .txt files
├── outputs/ # Final structured JSON results
├── src/ # Core logic (PDF parsing, vector store, QA)
└── README.md
```



---

## ✨ Sample Output (JSON)
```
{
"Scope 1 GHG Emissions": {
"answer": "6,515 tCO2e (75% reduction from baseline)",
"page_reference": "42",
"confidence_score": 0.95
},
"Net-Zero Target": {
"answer": "Achieve net-zero emissions by 2040 across all operations",
"page_reference": "15",
"confidence_score": 0.92
}
}
```

---

## 📜 License

Licensed under the MIT License. See `LICENSE` for more details.

---

## 👨‍💻 Author

**Vaibhav Sharma**   | Mumbai, India  
[🔗 GitHub](https://github.com/vaisharma16) • [🔗 LinkedIn](https://www.linkedin.com/in/vaibhavsharma16/)


