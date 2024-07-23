import csv

# Lista de funcionários
funcionarios = [
    [1, 'Ana', 'Financeiro'],
    [2, 'Carlos', 'TI'],
    [3, 'Beatriz', 'RH']
]

# Abrir o arquivo 'funcionarios.csv' para escrita
with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    # Escrever o cabeçalho
    escritor.writerow(['id', 'nome', 'departamento'])
    # Escrever as linhas de dados
    escritor.writerows(funcionarios)
