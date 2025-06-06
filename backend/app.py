from flask import Flask, request, jsonify
from flask_cors import CORS
from extractor import extract_text_from_pdf_file
import sqlite3
from dotenv import load_dotenv
from generator import generate_mcqs_from_text
from flask import render_template


load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files["file"]
    filename = file.filename

    if filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not filename.lower().endswith(".pdf"):
        return jsonify({"error": "Upload a valid PDF."}), 400

    # Extract text from PDF
    extracted_text = extract_text_from_pdf_file(file)

    # Store in database
    conn = sqlite3.connect("quizforge.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO documents (filename, content) VALUES (?, ?)", (filename, extracted_text))
    doc_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return jsonify({"message": "Upload successful", "doc_id": doc_id})


@app.route("/generate-quiz/<int:doc_id>", methods=["GET"])
def generate_quiz(doc_id):
    # Retrieve content from DB
    conn = sqlite3.connect("quizforge.db")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM documents WHERE id=?", (doc_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return jsonify({"error": "Document not found"}), 404

    text = row[0]
    quiz_data = generate_mcqs_from_text(text)

    return jsonify(quiz_data)  # quiz_data is already a structured dict

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
