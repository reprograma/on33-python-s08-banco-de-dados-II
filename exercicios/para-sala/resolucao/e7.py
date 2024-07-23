import csv

# Abrir o arquivo 'produtos.csv'
with open('produtos.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    # Ler e imprimir cada linha do arquivo CSV
    for linha in leitor:
        print(linha)
