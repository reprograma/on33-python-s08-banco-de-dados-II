import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS livros (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       titulo text not null,
       autor text not null,
       ano integer,
       preco real   
   )
   """)

conn.commit()
cursor.close()
conn.close()