
import csv

funcionarios = [
       ["Inteligência Emocional", "Daniel Goleman", 1995, 39.99],
       ["Código Limpo", "Robert C. Martin", 2008, 42.80],
       ["O Programador Pragmático", "Andrew Hunt, David Thomas", 1999, 40.00],
       ["Como Fazer Amigos e Influenciar Pessoas", "Dale Carnegie", 1936, 22.50],
       ["Transforme Sua Vida com o Poder da Mente", "Louise Hay", 2011, 20.00] 
    ]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile: # w da a permisão de escrita
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'autor', 'ano', 'preco']) # sempre tem qu emndar uma lista no caso id', 'nome', 'departamento'
    escritor.writerows(funcionarios) # sempre mandar lista no caso funcionarios

    # abertura de leitura e escrita

# writer escrever linas e writerows escrever varais linhas  
