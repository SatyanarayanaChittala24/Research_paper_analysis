# 📄 Research Paper Analysis RAG Assistant

[![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-4285F4?style=flat&logo=google-gemini&logoColor=white)](https://aistudio.google.com/)

A sophisticated **Retrieval-Augmented Generation (RAG)** application designed to streamline academic research. This tool indexes PDF research papers into a vector space, allowing users to ask natural language queries and receive answers grounded strictly in the document's content.

---

## 🔍 How the Query Process Works

When you type a question, the system doesn't just "guess"; it performs a mathematical search to find the most relevant parts of your PDF:


1.  **Query Embedding**: Your question is converted into a numerical vector (a list of coordinates).
2.  **Semantic Search**: The system compares your question's vector against the vectors of all text blocks in the PDF (stored in **FAISS**).
3.  **Context Retrieval**: The top 3 most relevant text "chunks" are pulled from the document.
4.  **Augmented Generation**: The retrieved text + your original question are sent to **Gemini 1.5 Flash** to generate a precise answer.

---

## 🛠️ Technological Architecture

| Layer | Component | Technology |
| :--- | :--- | :--- |
| **Interface** | Frontend | HTML ,CSS3 ,JavaScript |
| **Server** | Backend | Flask (Python) |
| **Extraction** | PDF Parsing | PyPDF |
| **Intelligence** | LLM | Google Gemini 1.5 Flash |
| **Memory** | Vector Database | FAISS (Facebook AI Similarity Search) |
| **Embeddings** | Text Vectorization | Google `text-embedding-004` |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/SatyanarayanaChittala24/Research_paper_analysis.git](https://github.com/SatyanarayanaChittala24/Research_paper_analysis.git)
cd Research_paper_analysis

2. Environment Configuration
Create a .env file in the backend/ directory:

```bash
# backend/.env
GEMINI_API_KEY=your_api_key_here
3. Running the Application
Start Backend:

```bash

cd backend
python app.py
Start Frontend: Open frontend/index.html in your web browser.

🚀 Usage Guide
Upload: Select a Research Paper (PDF). The system will "Index" it by breaking it into chunks and saving them into the FAISS vector database.

Query: Type a specific question in the chat box, such as "What is the methodology used in this study?"

Retrieve: The system scans the FAISS index, retrieves the most relevant information from the PDF, and provides a summarized, accurate answer.

