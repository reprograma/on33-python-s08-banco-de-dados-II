import csv
import sqlite3
# Conectar ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
dados = cursor.fetchall()   #fetchall busca oo que esta no select e guarda em dados

with open('exportados_livros.csv', 'w', newline='', 
encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile) # Defini  onde vai ser escrita 
        escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])  # Escrever cabeçalhos
        escritor.writerows(dados) # Escrever dados

#conn.commit()  nesse caso não precisa usar o commit o select não precisa usar o commit 
cursor.close()
conn.close()