# **Importação de CSV para SQLite**:
import sqlite3
import csv

conn = sqlite3.connect('livraria.db')  #conectar ao banco de dados
cursor = conn.cursor()

# ler dados csv e inserir na abela 


with open('livros.csv', newline='', encoding='utf-8') as csvfile:
       leitor = csv.reader(csvfile)
       next(leitor)  # next pula o cabecalho 
       for linha in leitor:
           cursor.execute("""
            INSERT INTO livros (titulo, autor, ano, preco)
            VALUES (?, ?, ?, ?)
            """, (linha[0], linha[1], linha[2], linha[3])) # corresponde linha [1] colunanome,linha[2] email 

conn.commit()
cursor.close()
conn.close()

