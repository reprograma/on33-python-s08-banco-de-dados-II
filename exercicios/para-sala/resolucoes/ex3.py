import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute ("SELECT * FROM estudantes")
registros = cursor.fetchall()

#fetchall:busca por todas as informações do select e encaminha para o registro

for registro in registros:
    print (registro)

cursor.close()
conn.close()
