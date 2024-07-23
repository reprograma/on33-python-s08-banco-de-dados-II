#2. **Importando Dados de um CSV**
   #- Crie um arquivo CSV chamado `livros.csv` com as colunas `titulo`, `autor`, `ano`, e `preco`.
   #- Adicione pelo menos 5 registros no arquivo `livros.csv 

import csv

novos_livros = [    
    [1,'Memórias Póstumas de Brás Cubas', 'Machado de Assis', '1881', '25.0'],
    [2,'Grande Sertão: Veredas', 'Guimarães Rosa', '1956', '30.0'],
    [3,'Morte e Vida Severina', 'João Cabral de Melo Neto', '1955', '60.0'],   
    [4,'Dom Casmurro', 'Machado de Assis', '1899', '40.0'],
    [5,'O Cortiço', 'Aluízio Azevedo', '1890', '50.0']
]

with open('livros.csv', 'w', newline ='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(novos_livros)


