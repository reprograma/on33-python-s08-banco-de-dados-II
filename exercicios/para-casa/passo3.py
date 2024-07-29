import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Selecionando e exibindo todos os registros
cursor.execute('SELECT * FROM livros')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fechando a conexão
conn.close()
