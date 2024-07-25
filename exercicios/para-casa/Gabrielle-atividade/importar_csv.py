import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

with open('livros.csv',  newline='', encoding='UTF-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor) 
    for linha in leitor:
        if len(linha) == 4:
            cursor.execute('INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)', (linha[0], linha[1], linha[2], linha[3]))


conn.commit()
cursor.close()
conn.close()