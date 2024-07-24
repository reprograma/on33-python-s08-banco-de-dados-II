import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

livro_id = 4


cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))

conn.commit()

print(f"Livro ID {livro_id} removido com sucesso.")

cursor.close()
conn.close()
