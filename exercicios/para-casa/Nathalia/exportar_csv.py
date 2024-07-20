#------------------------------------ PASSO 6 ------------------------------------
# - Escreva um script Python que exporte os dados da tabela `livros` para um novo arquivo CSV chamado `exportados_livros.csv`.
#---------------------------------------------------------------------------------

import sqlite3
import csv

#conexão com a database
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
               SELECT * 
               FROM livros
               """)
dados_tabela = cursor.fetchall()

with open('exportados_livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
        writer.writerows(dados_tabela)

conn.commit()
cursor.close()
conn.close()