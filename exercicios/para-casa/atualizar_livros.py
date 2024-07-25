import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("UPDATE livros SET preco = ? WHERE titulo = ?", (7.99, 'Harry Potter e a Criança Amaldiçoada'))

conn.commit()
cursor.close()
conn.close()