#------------------------------------ PASSO 2 ------------------------------------
#    - Crie um arquivo CSV chamado `livros.csv` com as colunas `titulo`, `autor`, `ano`, e `preco`.
#    - Adicione pelo menos 5 registros no arquivo `livros.csv`.
#    - Escreva um script Python que leia os dados do `livros.csv` e insira-os na tabela `livros`.
#---------------------------------------------------------------------------------

import sqlite3
import csv

#conexão com a database
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

#inserções no banco de dados
with open ('livros.csv', newline='', encoding='utf-8') as csvfile: #chama a função de leitura do arquivo csv
    leitor = csv.reader(csvfile)
    next(leitor) #pula o cabeçalho
    for linha in leitor:
        cursor.execute("""
                       INSERT INTO livros (titulo, autor, ano, preco) 
                       VALUES (?, ?, ?, ?)
                       """, linha)

conn.commit()
cursor.close()
conn.close()