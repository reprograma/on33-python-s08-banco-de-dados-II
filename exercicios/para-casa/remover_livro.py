# Atividade 5. Remover livro Tabela

import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM livros WHERE titulo = ?", ("Fazendo Meu Filme: A Estreia de Fani", ))

conn.commit()
cursor.close()
conn.close()