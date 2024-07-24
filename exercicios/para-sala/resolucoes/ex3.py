# Consulta de dados: 
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM estudantes")   # executa o select, só uma consulta
registros = cursor.fetchall() # busca toda a informação do select,captura ele e garda no registro p em segiuda ir p o for in, onde irá printar linha por linha.

for registro in registros:   # irá printar cada registro linha por linha, um looping até o último registro noo terminal
       print(registro)

cursor.close()  #não tem commit pois é só para consultar, no própio termminal
conn.close()
