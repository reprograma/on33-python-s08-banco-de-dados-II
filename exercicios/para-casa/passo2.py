import csv
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Lendo o arquivo CSV e inserindo os dados na tabela
with open('livros.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
            INSERT INTO livros (titulo, autor, ano, preco) 
            VALUES (?, ?, ?, ?)
        ''', (row['titulo'], row['autor'], row['ano'], row['preco']))

# Confirmando as mudanças e fechando a conexão
conn.commit()
conn.close()
