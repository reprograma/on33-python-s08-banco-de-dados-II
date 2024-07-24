import sqlite3  
import csv

conn = sqlite3.connect('livraria.db') 
cursor = conn.cursor()      

cursor.execute("""
   CREATE TABLE IF NOT EXISTS livros (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       Titulo TEXT NOT NULL,
       Autor TEXT NOT NULL,
       Ano INTERGER NOT NULL,
       Preco REAL NOT NULL
   )
   """)

with open('livros.csv', newline='', encoding='utf-8') as csvfile: 
       leitor = csv.reader(csvfile)
       next(leitor)  
       for linha in leitor:  
           cursor.execute("INSERT INTO livros (Titulo, Autor, Ano, Preco) VALUES (?, ?, ?, ?)", (linha[1], linha[2], linha[3], linha[4]))
            
conn.commit()
cursor.close()
conn.close()

