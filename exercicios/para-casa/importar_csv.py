import csv 

livros = [
    [10, 'Um Dia', 'David Nicholls', 2012, 40.37],
    [20,'Harry Potter e o Prisioneiro de Azkaban', ' J.K. Rowling', 2000, 52.42],
    [30, 'Harry Potter e as Relíquias da Morte', 'J.K. Rowling', 2007, 73.43],
    [40, 'Eclipse: (Série Crepúsculo)', ' Stephenie Meyer', 2008, 52.43],
    [50, 'Textos cruéis demais para serem lidos rapidamente', 'Igor Pires', 2017, 34.95]
]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    editor = csv.writer(csvfile)
    editor.writerow(['id','titulo', 'autor', 'ano', 'preco'])
    editor.writerows(livros)

 