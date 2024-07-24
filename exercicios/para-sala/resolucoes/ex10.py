# Exportação de SQLite para CSV 
# Escreva um script que exporte os dados da tabela `clientes` do banco de dados `empresa.db` 
# para um arquivo CSV chamado `exportados_clientes.csv

import csv
import sqlite3

conn = sqlite3.connect('empresa.db') 
cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")  # busca os dados no banco e armazena em dados
dados = cursor.fetchall() #busca o que está no select e garda os dados

with open('exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile: #cria o arquivo se existe ele sbstitui o que está dentro
        escritor = csv.writer(csvfile) #define a escrita/ abertura do arquivo que será criado após ser executado chamado exportados
        escritor.writerow(['id', 'nome', 'email']) # cria as linhas do cabeçalho
        escritor.writerows(dados) # escrita de múltiplas linhas exportando os dados serão guardados dentro 

cursor.close() 
conn.close()