import csv

livros = [
    [1, 'O Silmarillion', 'J.R.R. Tolkien', 2019, 59.70],
    [2, 'O Nome da Rosa', 'Umberto Eco', 2017, 99.90],
    [3, 'O Encontro Marcado', 'Fernando Sabino',1986, 65.35],
    [4, 'A Insustentável Leveza do Ser', 'Milan Kundera', 2014, 58.90],
    [5, 'Contos de Imaginação e Mistério', 'Edgar Allan Poe', 2012, 103.35],
    [6, 'O filósofo, a enfermeira e o trapaceiro', 'Max Velati', 2020, 50.50]
   ]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(livros)