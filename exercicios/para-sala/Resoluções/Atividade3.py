import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM estudantes")
registros = cursor.fetchall() #busca linha por linha

for registro in registros:
       print(registro)

cursor.close()
conn.close()