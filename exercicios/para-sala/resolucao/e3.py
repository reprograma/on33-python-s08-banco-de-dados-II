import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Selecionar todos os registros da tabela 'estudantes'
cursor.execute("SELECT * FROM estudantes")
registros = cursor.fetchall()

# Imprimir todos os registros
for registro in registros:
    print(registro)

# Fechar o cursor e a conexão
cursor.close()
conn.close()
