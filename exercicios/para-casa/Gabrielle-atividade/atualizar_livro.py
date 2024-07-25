import sqlite3
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
preco = [
 (29.99, 1),
]
cursor.executemany("UPDATE livros SET preco = ? WHERE id = ?", preco)
conn.commit()
cursor.close()
conn.close()

