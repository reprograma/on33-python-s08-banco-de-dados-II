import sqlite3
import csv

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Criar a tabela 'clientes' se ela não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Abrir o arquivo 'clientes.csv' e inserir os dados na tabela
with open('../clientes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # Pular o cabeçalho
    for linha in leitor:
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (linha[1], linha[2]))

# Confirmar a transação
conn.commit()

# Fechar o cursor e a conexão
cursor
