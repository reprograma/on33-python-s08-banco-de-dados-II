import csv
import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

with open('livros.csv', newline='', encoding='utf-8') as csvfile:
       leitor = csv.reader(csvfile)
       next(leitor) 
       for item in leitor:
           cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (item [0], item [1], item [2], item [3]))

conn.commit()
cursor.close()
conn.close()