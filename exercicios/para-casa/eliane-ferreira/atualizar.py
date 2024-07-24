import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Definir o ID do livro e o novo preço
livro_id = 6
novo_preco = 29.99

# Atualizar o preço do livro com o ID especificado
cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, livro_id))

conn.commit()

print(f"Preço do livro com ID {livro_id} atualizado para {novo_preco}.")

cursor.close()
conn.close()

