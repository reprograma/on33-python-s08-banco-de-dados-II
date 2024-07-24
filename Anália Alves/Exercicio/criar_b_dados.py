import sqlite3

# Conectar ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Criar a tabela 'livros'
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

# Fechar a conexão
cursor.close()
conn.close()

print("Banco de dados e tabela 'livros' criados com sucesso!")
