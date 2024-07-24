import sqlite3
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()
estudantes = [  #modelo de exercício para alterar dados de mais de um id
 (27, 'Alice'),
 (29, 'Bob'),
]
cursor.executemany("UPDATE estudantes SET idade = ? WHERE nome = ?", estudantes)
conn.commit()
cursor.close()
conn.close()