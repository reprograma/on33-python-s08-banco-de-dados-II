import csv
import sqlite3

livros = [
    [1, 'A Biblioteca da Meia-Noite', 'Matt Haig', 2021, 65.91],
    [2, 'Cleopatra e Frankenstein', 'Coco Mellors', 2023, 66.00],
    [3, 'Pessoas normais', 'Sally Rooney', 2019, 65.90],
    [4, 'Tudo o que eu sei sobre o amor', 'Dolly Alderton', 2022, 59.60],
    [5, 'Tudo é rio', 'Carla Madeira', 2021, 59.10],
    [6, 'O Hobbit', 'J.R.R. Tolkien', 2019, 56.25]
]

with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(livros)

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

with open('books.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)
    for linha in leitor:
        try:
            titulo = linha[1]
            autor = linha[2]
            ano = int(linha[3])
            preco = float(linha[4])
            cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (titulo, autor, ano, preco))
        except Exception as e:
            print(f'Erro na importação de dados. Linha: {linha} Erro: {e}')

conn.commit()
cursor.close()
conn.close()
