import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

estudantes = [
    ( 30, 'Alice'),
    (18, 'Bob',),
]

cursor.executemany("UPDATE estudantes SET idade = ? WHERE nome = ?", estudantes)

conn.commit()
cursor.close()
conn.close()
