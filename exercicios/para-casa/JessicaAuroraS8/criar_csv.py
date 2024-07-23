import csv

# Lista de livros
livros = [
    [1,'Lugar de Negro', 'Lelia Gonsalez', 1982, 27.10],
    [2,'Por um feminismo afro latino americano', 'Lelia Gonsalez', 1988, 30.30],
    [3,'O feminismo e para todo mundo', 'Bell Hooks', 2018, 21.50],
    [4,'O movimento negro educador', 'Nilma Lino Gomes' , 2017, 19.90],
    [5,'Pequeno Manual Antirracista', 'Djamila Ribeiro', 2019, 14.90]
]

# Inserindo informaçoes no arquivo csv
with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(livros)
