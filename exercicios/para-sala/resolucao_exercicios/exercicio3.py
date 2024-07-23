import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * from estudantes")
registros = cursor.fetchall() #Busca todos os casos (restantes) do conjunto de dados ativo ou, se houver divisões, os casos restantes na divisão atual. Se não houver linhas restantes, o resultado será uma tupla vazia..

for registro in registros:
    print(registro)

cursor.close()
conn.close()
