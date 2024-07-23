import csv 

livros= [
    [1,"A Culpa é das Estrelas", "John Green", 2012, 29.90],
    [2, "Quem é Você, Alasca?", "John Green", 2005, 35.90],
    [3, "P.S. Eu Te Amo", "Cecelia Ahern", 2004, 39.90],
    [4, "Cartas para Julieta", "Lise Friedman e Ceil Friedman", 2010, 49.90],
    [5, "Crepúsculo", "Stephenie Meyer", 2005, 39.90],
    [6, "Heartstopper", "Alice Oseman", 2018, 44.90],
    [7, "Para Todos os Garotos que Já Amei", "Jenny Han", 2014, 39.90]
]


with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id','Titulo', 'Autor', 'Ano', 'Preco'])
    escritor.writerows(livros)
