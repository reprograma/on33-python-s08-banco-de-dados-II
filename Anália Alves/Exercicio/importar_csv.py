import sqlite3
import csv

livros = [
    [1, 'Crime e Castigo', 'Fiódor Dostoiévski', 1866, 40.00],
    [2, 'O Sol é para Todos', 'Carlos Oliveira', 1960, 23.50],
    [3, 'Jane Eyre', 'Charlotte Brontë', 1847, 31.50],
    [4, 'Razão e Sensibilidade', 'Jane Austen', 1811, 30.00],
    [5, 'Anna Karenina', 'Liev Tolstói', 1877, 36.00],
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