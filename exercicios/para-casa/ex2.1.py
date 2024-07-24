import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

livros = [
    ('O Senhor dos Anéis: A Sociedade do Anel',"J.R.R. Tolkien",1954,60.00),
    ("O Senhor dos Anéis: As Duas Torres","J.R.R. Tolkien",1954,49.90),
    ("O Senhor dos Anéis: O Retorno do Rei","J.R.R. Tolkien",1955,89.90)
]

cursor.executemany("INSERT INTO livros  (titulo, autor, ano, preco) VALUES (?, ?, ?,?)", livros)

conn.commit()
cursor.close()
conn.close()