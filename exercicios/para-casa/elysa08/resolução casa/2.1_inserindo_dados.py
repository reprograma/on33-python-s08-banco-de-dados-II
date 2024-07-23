import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL, 
        ano INTEGER NOT NULL, 
        preco REAL               
)
""")


with open('livros.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  

    for linha in leitor:
        id = linha[0]
        titulo = linha[1]
        autor = linha[2]
        ano = linha[3]
        preco = linha[4] 

    
        cursor.execute("INSERT INTO livros (id, titulo, autor, ano, preco) VALUES (?, ?, ?, ?, ?)",
                       (id, titulo, autor, ano, preco))

conn.commit()
conn.close()

print("Inserção de dados concluída com sucesso!")