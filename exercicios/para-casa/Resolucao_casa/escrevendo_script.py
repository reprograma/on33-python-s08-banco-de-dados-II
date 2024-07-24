import csv
import sqlite3

conn = sqlite3.connect('livros.db')
cursor = conn.cursor()

# Criar a tabela livros (se ainda não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    preco REAL NOT NULL
)
''')

with open('livros.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
        INSERT INTO livros (titulo, autor, ano, preco) 
        VALUES (?, ?, ?, ?)
        ''', (row['titulo'], row['autor'], row['ano'], row['preco']))

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()


print("Inserção de dados concluída com sucesso!")



