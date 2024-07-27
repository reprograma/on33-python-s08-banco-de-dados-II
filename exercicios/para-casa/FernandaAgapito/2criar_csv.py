import csv

livros = [
    [1, "Eu, Robô", "Isaac Asimov", 1950,50.00],
    [2, "1984", "George Orwell", 1949,50.00],
    [3, "O Conto da Aia", "Margaret Atwood", 1985,50.00],
    [4, "Fahrenheit 451", "Ray Bradbury", 1953,50.00],
    [5, "A Guerra dos Mundos", "H.G. Wells", 1898,50.00],
    [6, "Solaris", "Stanisław Lem", 1961,50.00]
]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(livros)