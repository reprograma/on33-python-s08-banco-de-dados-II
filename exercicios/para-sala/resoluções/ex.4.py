import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

estudantes = [
    (28,'Alice'),
    (25,'Bob'),
]

cursor.executemany("UPDATE estudantes SET idade = ? WHERE nome = ?", estudantes)

conn.commit()
cursor.close()
conn.close()