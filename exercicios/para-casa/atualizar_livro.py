import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

novo_preco = 49.99
cursor.execute('''
UPDATE livros
SET preco = ?
WHERE id = 3
''', (novo_preco,))

conn.commit()

cursor.close()
conn.close()