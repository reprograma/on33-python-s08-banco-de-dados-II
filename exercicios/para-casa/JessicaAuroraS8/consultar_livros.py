import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Selecionar todos os registros da tabela 'livros'
cursor.execute("SELECT * FROM livros")
registros = cursor.fetchall()

# Imprimir todos os registros
for registro in registros:
    print(registro)

# Fechar o cursor e a conexão
cursor.close()
conn.close()
