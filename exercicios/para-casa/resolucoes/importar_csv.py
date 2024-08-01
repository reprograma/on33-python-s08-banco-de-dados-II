import csv


livros = [
    [1, 'A', 'Ana', '2200', '39,99'],
    [2, 'B', 'Maria', '2202', '30'],
    [3, 'C', 'João', '2203', '25'],
    [4, 'D', 'Bea', '2204', '40'],
    [5, 'E', 'Marcelie', '2205', '36'],
]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
   escritor = csv.writer(csvfile)
   escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
   escritor.writerows(livros)


