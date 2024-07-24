import csv

livros = [
    ["O Apanhador no Campo de Centeio", "J.D. Salinger", 1951, 39.90],
    ["Dom Casmurro", "Machado de Assis", 1899, 19.90],
    ["Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, 24.90],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 29.90],
    ["Harry Potter e a Câmara Secreta", "J.K. Rowling", 1998, 34.90]
]


with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(livros)