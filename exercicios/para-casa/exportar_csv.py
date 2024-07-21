#Atividade 5. Exportando tabela para CSV
import csv
import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
dados = cursor.fetchall()

with open('exportados_livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    livro = csv.writer(csvfile)
    livro.writerow(['id', 'titulo', 'autor', 'ano','preco'])
    livro.writerows(dados)

cursor.close()
conn.close()