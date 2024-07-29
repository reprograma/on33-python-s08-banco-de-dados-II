import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Removendo o livro com id 3
cursor.execute('''
    DELETE FROM livros
    WHERE id = 3
''')

# Confirmando as mudanças e fechando a conexão
conn.commit()
conn.close()
