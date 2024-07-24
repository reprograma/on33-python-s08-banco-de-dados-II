import csv

livros = [   
    [1, 'A Revolta de Atlas', 'Any Rand', 1943, 87.34],
    [2, 'O Alienista', 'Machado de Assis', 2021, 12.00],
    [3, 'As Seis lições', 'Ludwing Von Mises', 2018, 27.10],
    [4, 'O caminho da servidão','Friedrich August Hayek', 2010, 25.56],
    [5, 'Podres de Mimados - As consequências do sentimentalismo tóxico: 1', ' Theodore Dalrymple', 2015, 58.23],
    [6, 'A Moreninha', 'Joaquim Manuel de Macedo', 2020, 11.73],
    [7, 'A Voz na sua Cabeça', 'Ethan Kross', 2021, 50.30]
]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile: 
       escritor = csv.writer(csvfile)   
       escritor.writerow(['id', 'Titulo', 'Autor', 'Ano','Preco']) 
       escritor.writerows(livros) 

