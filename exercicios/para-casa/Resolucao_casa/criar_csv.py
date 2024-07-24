import csv

livros = [
       [1, 'w', 'Bete', '1999', '40,99'],
       [2, 'P', 'Lisa', '2005', '38,50'],
       [3, 'Q', 'Vilma', '2013', '25,90'],
       [4, 'R', 'Maya', '2015', '30'],
       [5, 'Y', 'Bela', '2020', '50']
   ]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
   escritor = csv.writer(csvfile)
   escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
   escritor.writerows(livros)


   