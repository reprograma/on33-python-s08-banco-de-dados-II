import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Criar a tabela 'livros' se ela não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL, 
    ano INTEGER NOT NULL,
    preco REAL NOT NULL   
)
""")

# Confirmar a transação
conn.commit()

# Fechar o cursor e a conexão
cursor.close()
conn.close()
