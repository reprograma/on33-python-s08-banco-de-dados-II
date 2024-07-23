import sqlite3
import csv

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS clientes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               email TEXT NOT NULL
               )
               """)

#aqui você vai ler as informações que estão no csv que já existe lá no arquivo clientes
with open('../clientes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor) #essa linha tem como função pular o cabeçalho

    #aqui você vai fazer um for que vai percorrer cada item que tem lá no arquivo clientes e para cada um deles vai fazer um insert no banco de dados "empresa" que criamos, inserindo o que está na posição 
    for item in leitor:
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (item[1], item[2]))

conn.commit()
cursor.close()
conn.close()

