# log_query.py
import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            scraped_data TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_query(case_type, case_number, filing_year, scraped_data):
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO queries (case_type, case_number, filing_year, scraped_data, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, str(scraped_data), datetime.now().isoformat()))
    conn.commit()
    conn.close()
