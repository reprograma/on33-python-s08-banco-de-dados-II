import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('livraria.db')
cur = conn.cursor()

# Selecionar todos os registros da tabela livros
cur.execute('SELECT * FROM livros')

# Obter todos os registros
registros = cur.fetchall()

# Exibir os registros
for registro in registros:
    print(registro)

# Fechar a conexão
conn.close()
