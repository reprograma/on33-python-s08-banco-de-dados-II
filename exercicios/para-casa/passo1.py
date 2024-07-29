import sqlite3

# Conectando ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Criando a tabela 'livros'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        ano INTEGER,
        preco REAL
    )
''')

# Confirmando as mudanças e fechando a conexão
conn.commit()
conn.close()
