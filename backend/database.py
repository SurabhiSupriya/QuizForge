import sqlite3

def init_db():
    conn = sqlite3.connect("quizforge.db")
    c = conn.cursor()

    # Documents table
    c.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        content TEXT
    )
    """)

    # Quizzes table
    c.execute("""
    CREATE TABLE IF NOT EXISTS quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doc_id INTEGER,
        question TEXT,
        answer TEXT,
        FOREIGN KEY(doc_id) REFERENCES documents(id)
    )
    """)

    # User scores table
    c.execute("""
    CREATE TABLE IF NOT EXISTS user_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quiz_id INTEGER,
        user_id TEXT,
        selected_answer TEXT,
        is_correct INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(quiz_id) REFERENCES quizzes(id)
    )
    """)

    conn.commit()
    conn.close()
