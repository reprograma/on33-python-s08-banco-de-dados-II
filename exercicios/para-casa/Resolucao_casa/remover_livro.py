import sqlite3
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM livros WHERE id = ?", ('4',))

conn.commit()
cursor.close()
conn.close()

print("Livro com id 4 removido com sucesso.")

