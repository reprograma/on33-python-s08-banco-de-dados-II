import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
cursor.execute("""
   CREATE TABLE IF NOT EXISTS livros (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       título TEXT NOT NULL,
       autor TEXT NOT NULL,        
       ano INTEGER,
       preço REAL
   )
   """)
