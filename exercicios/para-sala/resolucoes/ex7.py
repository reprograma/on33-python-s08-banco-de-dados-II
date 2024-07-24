# Leitura de CSV
import csv # irá importar o arquivo produtos.csv criado anteriormente

with open('produtos.csv', newline='', encoding='utf-8') as csvfile:  # neline representa a linha vazia no final da lista/ encoding é utilizado pois há palavras com acento. 
       leitor = csv.reader(csvfile) # o leitura do arquivo feito acima e armazenado 
       for linha in leitor: # usa-se o singular p informação única  
           print(linha)

# imprime as informações que estão dentro de csv.
