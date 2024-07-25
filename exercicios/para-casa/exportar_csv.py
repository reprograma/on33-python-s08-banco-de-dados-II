import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
dados = cursor.fetchall()

with open('exportando.csv', 'w', newline='', encoding='utf-8') as csvfile:
    editor = csv.writer(csvfile)
    editor.writerow(['id','titulo', 'autor', 'ano', 'preco'])
    editor.writerows(dados)

cursor.close()
conn.close()