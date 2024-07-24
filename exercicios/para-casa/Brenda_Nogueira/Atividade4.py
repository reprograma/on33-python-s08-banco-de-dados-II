import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("UPDATE livros SET preco = ? WHERE titulo = ?", (50.00, 'Harry Potter e a Pedra Filosofal'))
# ("UPDATE estudantes SET idade = 23 WHERE nome = 'Bob'") uma outra menira de fazer, mas não é tão segura

conn.commit()
cursor.close()
conn.close()