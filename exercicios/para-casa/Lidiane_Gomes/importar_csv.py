import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

with open('livros.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)
    for linha in leitor:
        try:
            titulo = linha[1]
            autor = linha[2]
            ano = int(linha[3])
            preco = float(linha[4])
            if not titulo or not autor or not ano or not preco:
                print(f'Há dados nulos na linha: ', linha)
            cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (titulo, autor, ano, preco))
        except Exception as e:
            print(f'Erro na importação de dados. Linha: {linha} Erro: {e}')


conn.commit()
cursor.close()
conn.close()