# **Atualização de Dados**:
import sqlite3
# Conectar ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (29.99, 1))
#mais de uma informação colocar o executemany

conn.commit()
cursor.close()
conn.close()

