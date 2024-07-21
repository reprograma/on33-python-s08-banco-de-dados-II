#Atividade 2. Importando Dados de um CSV

import sqlite3
import csv 

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       titulo TEXT NOT NULL,
       autor TEXTT NOT NULL,
       ano INTEGER NOT NULL,
       preco REAL NOT NULL
)
""")

with open('livros.csv', newline='', encoding='utf-8') as livrofile:
       livros = csv.reader(livrofile)
       next(livros) 
       for livro in livros:
              if len(livro) >= 6:
                     cursor.execute("INSERT INTO livros (id, titulo, autor, ano, preco) VALUES (?, ?, ?, ?, ?)", (livro[1], livro[2], livro[3], livro[4], livro[5]))
                     print(livro)
           
conn.commit()
cursor.close()
conn.close()
