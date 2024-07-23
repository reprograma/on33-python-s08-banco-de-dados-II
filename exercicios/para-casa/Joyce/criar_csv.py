import csv


livros = [
       [1, 'A garota no espelho', 'Rose Carlyle', 2022, 25.65],
       [2, 'Véspera', 'Carla Madeira', 2021, 37.90],
       [3, 'Ensaio sobre a cegueira', 'José Saramago', 2020, 34.87],
       [4, 'Tudo é rio' , 'Carla Madeira', 2018, 45.55],
       [5, 'Meu pé de laranja lima', 'José mauro de Vasconcelos', 2017, 42.88]
   ]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(livros)