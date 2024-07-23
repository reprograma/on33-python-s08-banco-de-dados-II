import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

estudantes = [
    (27, 'Alice'),
    (29, 'Bob'),
]

cursor.executemany("UPDATE estudantes SET idade = ? WHERE nome = ?", estudantes)

conn.commit()
cursor.close()
conn.close()

#para alterar vários valores, poderíamos trazer uma lista do que queremos atualizar e poderíamos dar um cursor.executemany
