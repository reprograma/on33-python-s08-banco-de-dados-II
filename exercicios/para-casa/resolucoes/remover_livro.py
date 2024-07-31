import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

id = '7'

cursor.execute("DELETE FROM livros WHERE id = ?", (id))

conn.commit()
cursor.close()
conn.close()