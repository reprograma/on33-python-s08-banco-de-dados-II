import sqlite3
import csv

# Conectar ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Selecionar todos os registros da tabela livros
cursor.execute("SELECT * FROM livros")
dados = cursor.fetchall()

# Definir o nome do arquivo CSV
catalogo_livros = 'exportados_livros.csv'

# Escrever os dados no arquivo CSV
with open(catalogo_livros, mode='w', newline='', encoding='utf-8') as csvfile:
    escritor_csv = csv.writer(csvfile)
    
    # Escrever o cabeçalho
    escritor_csv.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    
    escritor_csv.writerows(dados)

cursor.close()
conn.close()

print(f"Dados exportados para {catalogo_livros} com sucesso!")
