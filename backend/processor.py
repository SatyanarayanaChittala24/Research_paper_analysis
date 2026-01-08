import os
import numpy as np
import faiss
from pypdf import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Correctly Load the API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") # This matches the name in your .env file

if not api_key:
    print("❌ ERROR: API Key not found. Check your .env file!")
else:
    genai.configure(api_key=api_key)

class PaperProcessor:
    def __init__(self):
        self.index = None
        self.chunks = []

    def extract_text(self, pdf_path):
        print(f"\n[1/4] Reading PDF: {os.path.basename(pdf_path)}")
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                content = page.extract_text()
                if content:
                    text += content + "\n"
            return text
        except Exception as e:
            print(f"❌ PDF Read Error: {e}")
            return ""

    def create_vector_db(self, pdf_path):
        text = self.extract_text(pdf_path)
        if not text.strip():
            print("❌ No text extracted from PDF.")
            return False

        # [2/4] Chunking
        self.chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        print(f"[2/4] Created {len(self.chunks)} text blocks.")
        
        try:
            # [3/4] Creating Embeddings
            print("[3/4] Generating Embeddings via Gemini API...")
            embeddings = []
            for chunk in self.chunks:
                # Use a specific model name
                res = genai.embed_content(model="models/text-embedding-004", content=chunk)
                embeddings.append(res['embedding'])
            
            # [4/4] Loading into FAISS
            embeddings_np = np.array(embeddings).astype('float32')
            dimension = embeddings_np.shape[1]
            self.index = faiss.IndexFlatL2(dimension)
            self.index.add(embeddings_np)
            
            print("🚀 [DONE] FAISS Index is live and ready for questions!")
            return True
        except Exception as e:
            print(f"❌ API/FAISS ERROR: {e}") # This will show the exact error in terminal
            return False

    def query(self, user_question):
        if self.index is None:
            return "Please upload and index a document first."
            
        try:
            # Get question embedding
            res = genai.embed_content(model="models/text-embedding-004", content=user_question)
            q_emb = np.array([res['embedding']]).astype('float32')
            
            # Search
            D, I = self.index.search(q_emb, k=3)
            retrieved_context = "\n".join([self.chunks[i] for i in I[0] if i != -1])

            model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')
            prompt = f"Context: {retrieved_context}\n\nQuestion: {user_question}"
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Detailed Error: {e}")
            return f"Query Error: {str(e)}"