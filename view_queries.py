import sqlite3

conn = sqlite3.connect('queries.db')
c = conn.cursor()

c.execute("SELECT * FROM queries ORDER BY timestamp DESC")
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()
