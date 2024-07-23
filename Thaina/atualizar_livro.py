import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("UPDATE livros SET preco = ? WHERE titulo = ?", (100, 'Introdução à Programação com Python'))

conn.commit()
cursor.close()
conn.close()