import csv

with open('produtos.csv', encoding="UTF-8", newline='') as csvfile:
    linhas = csv.reader(csvfile)
    for linha in linhas:
        print(linha)
