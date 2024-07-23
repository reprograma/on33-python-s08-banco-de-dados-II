import sqlite3
import csv

livros = [
    [1, 'Introdução à Programação com Python', 'Ana Silva', 2020, 59.90],
    [2, 'Desenvolvimento Web Moderno', 'Carlos Oliveira', 2018, 89.90],
    [3, 'Algoritmos e Estruturas de Dados', 'Beatriz Souza', 2019, 74.90],
    [4, 'Inteligência Artificial: Conceitos e Aplicações', 'Marcelie Santos', 2021, 99.90],
    [5, 'Design de Jogos', 'João Pereira', 2017, 64.90],
    [6, 'Engenharia de Software', 'Paula Mendes', 2022, 79.90]
]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
       escritor = csv.writer(csvfile)
       escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preço'])
       escritor.writerows(livros)


conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
with open('livros.csv', newline='', encoding='utf-8') as csvfile:
       leitor = csv.reader(csvfile)
       next(leitor)  # Pular o cabeçalho
       for item in leitor:
           cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (item[1], item[2], item [3], item [4]))

conn.commit()
cursor.close()
conn.close()