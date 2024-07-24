import csv


livros = [
    [1, 'Biblia Sagrada', 'Sociedade Biblica do Brasil', '1500ac', '79,99'],
    [2, 'É assim que começa', 'Colleen Hoover', '2023', '48,90'],
    [3, 'É assim que acaba', 'Colleen Hoover', ' 2024', '54,90'],
    [4, 'Diário de um banana', 'Jeff Kinney', '2022', '40,89'],
    [5, 'A psicologia financeira', 'Morgan Housel', '2023', '49,90'],
]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
   escritor = csv.writer(csvfile)
   escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
   escritor.writerows(livros)