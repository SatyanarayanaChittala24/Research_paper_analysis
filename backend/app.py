from flask import Flask, request, jsonify
from flask_cors import CORS
from processor import PaperProcessor
import os

app = Flask(__name__)
CORS(app) # Allows local communication
processor = PaperProcessor()

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not os.path.exists('uploads'): os.makedirs('uploads')
    path = os.path.join("uploads", file.filename)
    file.save(path)
    
    # Run the indexing logic
    if processor.create_vector_db(path):
        return jsonify({"message": "Successfully indexed!"})
    else:
        return jsonify({"error": "Failed to read PDF text."}), 500

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    answer = processor.query(data.get("question"))
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(port=5000, debug=True)