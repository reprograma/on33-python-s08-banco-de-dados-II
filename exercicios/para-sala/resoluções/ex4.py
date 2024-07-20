import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (20, 'Bob'))

conn.commit()
cursor.close()
conn.close()
   