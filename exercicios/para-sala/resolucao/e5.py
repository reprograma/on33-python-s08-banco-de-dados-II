import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Deletar o estudante chamado 'Charlie'
cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

# Confirmar a transação
conn.commit()

# Fechar o cursor e a conexão
cursor.close()
conn.close()
