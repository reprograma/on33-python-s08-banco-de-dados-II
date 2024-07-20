#------------------------------------ PASSO 3 ------------------------------------
# - Escreva um script Python que selecione e exiba todos os registros da tabela `livros`.
#---------------------------------------------------------------------------------

import sqlite3

#conexão com a database
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
               SELECT * 
               FROM livros
               """)
itens = cursor.fetchall()

for item in itens:
    print(item)

cursor.close()
conn.close()