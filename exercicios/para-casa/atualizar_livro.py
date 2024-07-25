import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("UPDATE livros SET preco = ? WHERE titulo = ?", (50.21, 'Um Dia'))

conn.commit()
cursor.close()
conn.close()