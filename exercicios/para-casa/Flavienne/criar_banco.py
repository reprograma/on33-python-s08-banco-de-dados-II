import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS livros (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       Titulo TEXT NOT NULL,
       Autor TEXT NOT NULL,
       Ano INTERGER NOT NULL,
       Preco REAL NOT NULL
   )
   """)

conn.commit()
cursor.close()
conn.close() 

