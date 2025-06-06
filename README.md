# 🧠 QuizForge – AI-Powered MCQ Generator from PDFs

QuizForge is an AI-driven web application that automatically generates multiple-choice quizzes from PDF documents. It uses natural language processing (NLP) techniques to extract content, understand context, and create structured questions with options.


## ✨ Features

- 📝 Upload any PDF document
- 🧠 Automatically generate quiz questions
- ❓ Structured output with question, options, and correct answer
- 🧠 Supports lightweight **T5-based models** and optional **LLaMA 3 (local)** for advanced reasoning
- 💡 Designed to run **locally** without requiring GPU
- ⚡ Minimal frontend to preview questions directly in your browser


## 🏗 Tech Stack

- **Backend**: Flask, Transformers, PyTorch, sqlite3
- **Frontend**: HTML + JS (served via Flask)
- **AI Models**: 
  - `valhalla/t5-base-e2e-qg` (default, fast)
  - `meta-llama/Meta-Llama-3-8B-Instruct` *(optional, for deeper question generation)*


## 🚀 Getting Started

### 1. Clone the repo


git clone https://github.com/your-username/QuizForge.git
cd QuizForge

**2. Create and activate a virtual environment**

python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

**3. Install dependencies**
pip install -r requirements.txt

**4. Run the app**

cd backend
python app.py
Open your browser and visit:
👉 http://127.0.0.1:5000
