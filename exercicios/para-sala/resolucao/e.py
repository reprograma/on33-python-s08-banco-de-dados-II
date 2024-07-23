import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('estudantes')
cursor = conn.cursor()

# Criar a tabela 'estudantes' se ela não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Confirmar a transação
conn.commit()

# Fechar o cursor e a conexão
cursor.close()
conn.close()
