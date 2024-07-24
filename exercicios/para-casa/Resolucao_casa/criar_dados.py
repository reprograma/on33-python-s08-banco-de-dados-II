import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Criar a tabela livros
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    preco REAL NOT NULL
)
''')

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados 'livraria.db' e tabela 'livros' criados com sucesso.")

