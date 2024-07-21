# Atividade 4. tualizando Dados

import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("UPDATE livros SET preco = ? WHERE titulo = ?", ("R$ 39,99", "Orgulho e Preconceito"))

conn.commit()
cursor.close()
conn.close()