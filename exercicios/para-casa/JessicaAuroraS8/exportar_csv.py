import sqlite3
import csv

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Selecionar todos os registros da tabela 'livros'
cursor.execute("SELECT * FROM livros")
registros = cursor.fetchall()

# Abrir o arquivo 'exportados_livros.csv' para escrita
with open('exportados_livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    # Escrever o cabeçalho
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    # Escrever as linhas de dados
    escritor.writerows(registros)

    # Fechar o cursor e a conexão
cursor.close()
conn.close()

