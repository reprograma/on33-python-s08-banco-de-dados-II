import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM livros WHERE titulo = ?", ('O filósofo, a enfermeira e o trapaceiro', ))

conn.commit()
cursor.close()
conn.close()