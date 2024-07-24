import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Atualizar o preço do livro com id 1
novo_preco = 29.99
livro_id = 2

cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, livro_id))
conn.commit()

# Verificar se a atualização foi realizada
cursor.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
livro_atualizado = cursor.fetchone()


# Fechar a conexão
conn.close()
