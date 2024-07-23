import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Atualizar o preço do livro
cursor.execute("UPDATE livros SET preco = ? WHERE titulo = ?", (29.99, 'Por um feminismo afro latino americano'))

# Confirmar a transação
conn.commit()

# Fechar o cursor e a conexão
cursor.close()
conn.close()
