import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

with open('livros.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor) #pula o cabeçalho 'id, nome, email'
    for linha in leitor:
        cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (linha[0], linha[1], linha[2], linha[3]))

conn.commit()
cursor.close()
conn.close()