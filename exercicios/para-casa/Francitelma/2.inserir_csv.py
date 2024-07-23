#- Escreva um script Python que leia os dados do `livros.csv` e insira-os na tabela `livros`.

import sqlite3
import csv
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       titulo TEXT NOT NULL,
       autor TEXT NOT NULL,
       ano INTEGER NOT NULL,
       preco REAL NOT NULL)
    """)

with open('livros.csv', newline='', encoding='utf-8') as csvfile:
       leitor = csv.reader(csvfile)
       next(leitor)  #Pular o cabeçalho
       for linha in leitor:           
           cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (linha[1], linha[2], linha[3], linha[4]))


conn.commit() 
cursor.close()
conn.close()

