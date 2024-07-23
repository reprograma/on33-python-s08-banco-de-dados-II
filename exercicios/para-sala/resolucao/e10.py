import sqlite3
import csv

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Selecionar todos os dados da tabela 'clientes'
cursor.execute("SELECT * FROM clientes")
dados = cursor.fetchall()

# Abrir o arquivo 'exportados_clientes.csv' para escrita
with open('exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    # Escrever o cabeçalho
    escritor.writerow(['id', 'nome', 'email'])
    # Escrever as linhas de dados
    escritor.writerows(dados)

# Fechar o cursor e a conexão
cursor.close()
conn.close()
