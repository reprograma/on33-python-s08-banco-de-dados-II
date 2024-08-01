import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

livros = [
    ('F', 'João', 2020, 25.99),   
   ]

cursor.executemany("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", livros)

conn.commit()
cursor.close()
conn.close()

