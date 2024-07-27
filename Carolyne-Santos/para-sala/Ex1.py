import sqlite3
print(sqlite3.sqlite_version)

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS estudantes (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
       idade INTEGER NOT NULL
   )
   """)

conn.commit()
cursor.close()
conn.close()
