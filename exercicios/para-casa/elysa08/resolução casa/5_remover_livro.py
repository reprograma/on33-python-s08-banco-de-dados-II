import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

livro_id = 3

cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))

conn.commit()
conn.close()

print(f"Livro com id {livro_id} removido.")
