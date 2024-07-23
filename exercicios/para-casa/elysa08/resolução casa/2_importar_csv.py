import csv


livros = [
    [1, 'Aventuras de Mariana', 'Rosalie Ferreira', '2200', '39,99'],
    [2, 'O Mistério do Castelo Assombrado', 'Maria Delacruz', '2002', '30'],
    [3, 'O Tesouro Perdido de Atlântida', 'João Santos', '2003', '25'],
    [4, 'A Última Profecia', 'Beatriz Rosas', '2024', '40'],
    [5, 'Segredos do Universo', 'Pedro Mozart', '2205', '36'],
]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
   escritor = csv.writer(csvfile)
   escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
   escritor.writerows(livros)
