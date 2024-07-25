import sqlite3

conn = sqlite3.connect('escola.db') #o nome conn é uma convesão dos devs
cursor = conn.cursor()

estudantes = [
    ('Alice', 21),
    ('Bob', 22),
    ('Charlie', 23)
]

cursor.executemany('INSERT INTO estudantes (nome, idade) VALUES (?,?)', estudantes)

conn.commit()
cursor.close()
conn.close()