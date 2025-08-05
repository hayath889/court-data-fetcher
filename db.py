# db.py
import sqlite3

def init_db():
    conn = sqlite3.connect("queries.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_query(case_type, case_number, filing_year):
    conn = sqlite3.connect("queries.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO queries (case_type, case_number, filing_year)
        VALUES (?, ?, ?)
    ''', (case_type, case_number, filing_year))
    conn.commit()
    conn.close()
