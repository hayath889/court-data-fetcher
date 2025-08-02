from flask import Flask, request, render_template
import sqlite3
from scraper import fetch_case_details

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    try:
        data = fetch_case_details(case_type, case_number, filing_year)
        save_to_db(case_type, case_number, filing_year, data)
        return render_template('result.html', data=data)
    except Exception as e:
        return f"❌ Error: {str(e)}"

def save_to_db(case_type, case_number, filing_year, data):
    conn = sqlite3.connect("db.sqlite")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, case_type TEXT, case_number TEXT, year TEXT, data TEXT)")
    cur.execute("INSERT INTO logs (case_type, case_number, year, data) VALUES (?, ?, ?, ?)", 
                (case_type, case_number, filing_year, str(data)))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
