import sqlite3
import csv

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Abrir o arquivo 'livros.csv' e inserir os dados na tabela
with open('livros.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # Pular o cabeçalho
    for linha in leitor:
        cursor.execute("INSERT INTO livros (titulo, autor, ano, preco ) VALUES (?, ?, ?, ?)", (linha[1], linha[2], linha[3], linha[4]))

# Confirmar a transação
conn.commit()

# Fechar o cursor e a conexão
cursor.close()
conn.close()
