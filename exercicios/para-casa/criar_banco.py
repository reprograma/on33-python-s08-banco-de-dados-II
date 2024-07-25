import sqlite3
import csv

#criação e conexão da database
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

#criação da tabela principal
cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER NOT NULL,
            preco REAL NOT NULL
)
""")

conn.commit()
cursor.close()
conn.close()