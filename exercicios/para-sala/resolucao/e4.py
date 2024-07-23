import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Atualizar a idade do estudante 'Bob' para 23
cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))

# Confirmar a transação
conn.commit()

# Fechar o cursor e a conexão
cursor.close()
conn.close()
