#aqui estamos lendo um arquivo csv já existente (produtos.csv). 

#primeiro importamos o módulo csv
import csv

#aqui vamos definir o leitor
with open('produtos.csv', newline='', encoding='utf-8') as csvfile: #com (with) a função open, abra produtos.csv, considerando a nova linha sempre em branco e usando como padrão a formatação de utf-8 (a que se usa no Brasil, com acento etc.) e abra tudo isso como um arquivo csv (csvfile)
    leitor = csv.reader(csvfile) #aqui definimos uma variável "leitor", que é um reader e vai ler esse csvfile 
    for linha in leitor: #fazemos um for aqui, para cada item (linha) dentro do leitor
     print(linha) #aqui imprime na tela cada linha existente dentro desse leitor

