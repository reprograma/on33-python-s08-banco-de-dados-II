import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM livros WHERE titulo = ?", ('Textos cruéis demais para serem lidos rapidamente',))

conn.commit()
cursor.close()
conn.close()