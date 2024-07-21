import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("UPDATE livros SET preço = ? WHERE título = ?", (50, 'Macunaíma'))

conn.commit()
cursor.close()
conn.close()