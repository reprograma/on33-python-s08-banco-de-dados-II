import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudantes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )                   
""")
#aspas trplas quando tem mais de uma linha 

conn.commit() 
cursor.close()
conn.close()