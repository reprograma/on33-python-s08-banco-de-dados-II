# 6. **Exportando Dados para CSV**
  # - Escreva um script Python que exporte os dados da tabela `livros` para um novo arquivo CSV chamado `exportados_livros.csv`.

import csv
import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("SELECT id, titulo, autor, ano, preco FROM livros")
dados = cursor.fetchall()

with open('exportados_livros.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    escritor_csv.writerows(dados)

cursor.close()
conn.close()
