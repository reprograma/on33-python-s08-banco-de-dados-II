import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

novo_preco = 29.99
livro_id = 1

cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, livro_id))

conn.commit()
conn.close()

print(f"Preço do livro com id {livro_id} atualizado para {novo_preco}.")
