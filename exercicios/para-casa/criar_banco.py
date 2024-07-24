import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    ano INTEGER,
    preco REAL
)
''')

livros = [
["Feminismo é para Todo Mundo","bell hooks",2000,25.99],
["Irmã Outsider","Audre Lorde",1984,19.99],
["Quarto de Despejo: Diário de uma Favelada","Carolina Maria de Jesus",1960,29.99],
["Ponciá Vicêncio","Conceição Evaristo",2003,15.99],
["Olhos d'água","Conceição Evaristo",2014,22.99],
]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(livros)


conn.commit()

cursor.close()
conn.close()