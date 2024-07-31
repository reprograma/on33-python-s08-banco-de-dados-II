import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Exemplo com id:
cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (55.00, '2'))
# Exemplo com coluna Titulo:
cursor.execute("UPDATE livros SET preco = ? WHERE titulo = ?", (125.00, 'The Hobbit'))

conn.commit()
cursor.close()
conn.close()