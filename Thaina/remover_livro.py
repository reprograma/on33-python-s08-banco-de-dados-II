import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM livros WHERE titulo = ?", ('Introdução à Programação com Python', ))

conn.commit()
cursor.close()
conn.close()