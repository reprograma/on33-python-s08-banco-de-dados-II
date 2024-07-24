# Importação de CSV para SQLite - Importação de CSV para SQLite: 
# Crie um script que leia um arquivo CSV chamado `clientes.csv` 
# e insira os dados em uma tabela `clientes` no banco de dados SQLite `empresa.db`. A tabela deve ter as colunas `id`, `nome`, `email`.
import sqlite3  # utiliza o banco de dados junto ao csv
import csv

conn = sqlite3.connect('empresa.db') #variável qe contém a conexão com o banco
cursor = conn.cursor()      
# cria a tabela clientes
cursor.execute("""
   CREATE TABLE IF NOT EXISTS clientes (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
       email TEXT NOT NULL
   )
   """)

#Abrir o arquivo clientes.csv 
with open('../clientes.csv', newline='', encoding='utf-8') as csvfile: # .. indica que a pasta cliente está uma pasta abaixo deste exercício, logo  escrevo:  ../ p ter seus dados, ao invés de arrastar.
       leitor = csv.reader(csvfile)
       next(leitor)  # Pular o cabeçalho
       for linha in leitor: # execta linha por linha 
           cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (linha[1], linha[2])) # armazena o arquivo no banco de dados

# Confirmar a transação
conn.commit()
#Fechar o cursor e a conexão
cursor.close()
conn.close()

# armazenar o arquivo csv no banco de dados