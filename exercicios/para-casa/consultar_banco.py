# Atividade 3. Consultando e Exibir Dados

import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM livros')
registros = cursor.fetchall()

for livro in registros:
    print(livro)

cursor.close()
conn.close()