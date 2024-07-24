import csv

livros = [
       [1, 'Como Fazer Amigos e Influenciar Pessoas', 'Dale Carnegie', '2019', '31.90'],
       [2, 'Fundamentos da arquitetura de Software', 'Mark Richards', '2024', '69.20'],
       [3, 'Em busca de mim', 'Viola Davis', '2022', '14.90'],
       [4, 'Harry Potter e a Pedra Filosofal', 'J.K. Rowling', '2015', '40'],
       [5, 'O Livro de Receitas de Hogwarts', 'Rita Mock-Pike', '2,23', '81.50'],
       [6, 'Dom Casmurro', 'Machado de Assis', '2012', '25']
   ]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor','ano', 'preco'])
    escritor.writerows(livros)