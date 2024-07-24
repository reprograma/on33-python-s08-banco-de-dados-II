import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

livros = [
 (29.99, 1)
]

cursor.executemany("UPDATE livros SET preco = ? WHERE id = ?", livros)

conn.commit()
cursor.close()
conn.close()