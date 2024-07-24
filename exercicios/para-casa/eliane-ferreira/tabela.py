import sqlite3

conn = sqlite3.connect('livravia.db')

cursor = conn.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS livros (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       titulo TEXT NOT NULL,
       autor TEXT NOT NULL,
       ano TEXT NOT NULL,
       preco real
       
   )
   """)
conn.commit()
cursor.close()
conn.close()
