# atualizando o valor do preço do livro com id = 1 para 200 reais

import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()



cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (200, 1))

conn.commit()
cursor.close()
conn.close()