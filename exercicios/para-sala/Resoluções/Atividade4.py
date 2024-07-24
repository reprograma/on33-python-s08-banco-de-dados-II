import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))
# ("UPDATE estudantes SET idade = 23 WHERE nome = 'Bob'") uma outra menira de fazer, mas não é tão segura

conn.commit()
cursor.close()
conn.close()