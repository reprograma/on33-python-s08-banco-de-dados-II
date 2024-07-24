#  Escreva um script que crie um arquivo CSV chamado `funcionarios.csv` com as colunas `id`, `nome`, `departamento`.
import csv # indica uma escrita em CSV 

funcionarios = [
       [1, 'Ana', 'Financeiro'],
       [2, 'Carlos', 'TI'],
       [3, 'Beatriz', 'RH']
   ]
# lista de dados dos funcionários, inserida em uma lista chamada funcionários

with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile: # o  W (write) indica a permissão da escrita no arquivo
       escritor = csv.writer(csvfile)    # o arquivo 
       escritor.writerow(['id', 'nome', 'departamento']) # acrescenta uma linha  p cabeçalho
       escritor.writerows(funcionarios) # acrescenta mais de uma linha


# irá criar um arquivo escrito, chamado funcionarios.csv caso não existir
