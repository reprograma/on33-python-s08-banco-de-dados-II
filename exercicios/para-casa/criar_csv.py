import csv

livros = [
    [1, 'Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997, 8.99],
    [2, 'Harry Potter e a Câmara Secreta', 'J.K. Rowling', 1998, 9.99],
    [3, 'Harry Potter e o Prisioneiro de Azkaban', 'J.K. Rowling', 1999, 8.99],
    [4, 'Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000, 8.99],
    [5, 'Harry Potter e a Ordem da Fênix', 'J.K. Rowling', 2003, 9.99],
    [6, 'Harry Potter e o Enigma do Príncipe', 'J.K. Rowling', 2005, 9.99],
    [7, 'Harry Potter e as Relíquias da Morte', 'J.K. Rowling', 2007, 9.99],
    [8, 'Harry Potter e a Criança Amaldiçoada', 'J.K. Rowling, Jack Thorne, John Tiffany', 2016, 9.99]
   ]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(livros)