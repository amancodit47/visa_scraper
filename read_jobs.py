import sqlite3

conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM jobs')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
