# 📄 Research Paper Analysis RAG Assistant

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-4285F4?style=flat&logo=google-gemini&logoColor=white)](https://aistudio.google.com/)

An advanced **Retrieval-Augmented Generation (RAG)** system that allows users to chat with PDF research papers. This tool uses semantic search to retrieve relevant information and provide AI-generated insights based on document context.

---

## 🔍 How the Query & Retrieval Works

When you ask a question, the system follows a technical pipeline to ensure accuracy:



| Step | Action | Description |
| :--- | :--- | :--- |
| **1** | **Query Vectorization** | Your question is converted into a high-dimensional vector using Google Embeddings. |
| **2** | **Semantic Retrieval** | The system searches the **FAISS Index** to find the top 3 most relevant text blocks from the PDF. |
| **3** | **Context Feeding** | These 3 blocks are "fed" to the LLM as the only source of truth. |
| **4** | **Grounded Response** | Gemini 1.5 Flash generates an answer based *only* on the retrieved information. |

---

## 🛠️ Technological Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Large Language Model** | Gemini 1.5 Flash | Reasoning and Natural Language Generation |
| **Vector Database** | FAISS | Efficient similarity search for document chunks |
| **Embeddings** | Text-Embedding-004 | Converting text into mathematical representations |
| **Backend** | Flask (Python) | API orchestration and file management |
| **Frontend** | Vanilla JS / CSS3 | Responsive user interface for chat interaction |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/SatyanarayanaChittala24/Research_paper_analysis.git](https://github.com/SatyanarayanaChittala24/Research_paper_analysis.git)
cd Research_paper_analysis
