import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Deletar o livro com o título 'Lugar de Negro'
cursor.execute("DELETE FROM livros WHERE titulo = ?", ('Lugar de Negro',))

# Confirmar a transação
conn.commit()

# Fechar o cursor e a conexão
cursor.close()
conn.close()

