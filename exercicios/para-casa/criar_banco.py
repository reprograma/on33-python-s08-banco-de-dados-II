#Atividade 1. Criando o Banco de Dados e a Tabela
     
import sqlite3

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

conn.commit()
cursor.close()
conn.close()