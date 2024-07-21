import csv

livros = [
       [1, 'Orgulho e Preconceito','Jane Austen',1813, "R$30,00"],
       [2, 'O Senhor dos Anéis: A Sociedade do Anel','J.R.R. Tolkien',1954, "R$45,00"],
       [3, 'Dom Quixote','Miguel de Cervantes',1605, "R$50,00"],
       [4, 'O Sol é Para Todos','Harper Lee',1960, "R$35,00"],
       [5, 'Fazendo Meu Filme: A Estreia de Fani','Paula Pimenta',2008,"R$35,00"]
   ]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
       escritor = csv.writer(csvfile)
       escritor.writerow(['titulo','autor','ano','preco'])
       escritor.writerows(livros)