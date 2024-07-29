import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Atualizando o preço do livro com id 1
cursor.execute('''
    UPDATE livros
    SET preco = 29.99
    WHERE id = 1
''')

# Confirmando as mudanças e fechando a conexão
conn.commit()
conn.close()
