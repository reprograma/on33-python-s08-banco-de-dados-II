import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM estudantes") #aspas duplas uma linha só
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close
conn.close 