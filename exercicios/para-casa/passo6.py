import csv
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Selecionando todos os registros
cursor.execute('SELECT * FROM livros')
rows = cursor.fetchall()

# Escrevendo os dados para um novo arquivo CSV
with open('exportados_livros.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])  # Cabeçalho
    writer.writerows(rows)

# Fechando a conexão
conn.close()
