import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()


cursor.execute("DELETE FROM livros WHERE titulo = ?", ('Harry Potter e a Criança Amaldiçoada', ))

conn.commit()
cursor.close()
conn.close()