# 2. CRIANDO O ARQUIVO CSV

import csv

#Vamos realizar uma escrita em csv. Nesse caso, como não há um arquivo csv com o nome que iremos utilizar (livros), vamos escrever (write) o que queremos que esteja inserido nesse arquivo csv e o próprio comando de escrita, por não encontrar um arquivo com esse nome, entende que deve fazer a criação do arquivo.

#abaixo estamos criando a variável livros, que é uma lista de listas variadas (ou seja, com várias informações), porque contém vários dados dos livros
livros = [
    [1, 'A Invenção do Racismo na Antiguidade', 'Mário Sérgio Conti', 2021, 39.90],
    [2, 'Quarto de Despejo: Diário de uma Favelada', 'Carolina Maria de Jesus', 1960, 29.90],
    [3, 'Pequeno Manual Antirracista', 'Djamila Ribeiro', 2019, 24.90],
    [4, 'Olhares Negros: Raça e Representação', 'Bell Hooks', 1992, 34.90],
    [5, 'Eu Sei Por Que o Pássaro Canta na Gaiola', 'Maya Angelou', 1969, 42.90],
    [6, 'Racismo Estrutural', 'Silvio Almeida', 2019, 36.90],
    [7, 'O Genocídio do Negro Brasileiro', 'Abdias do Nascimento', 1978, 49.90]
]

#aqui estamos de fato fazendo a criação desse csv com esses comandos abaixo
with open ('livros.csv', 'w', newline='', encoding='utf-8') as csvfile: #aqui falamos: com (with) a função open, abra (ou crie) todas essas coisas aqui (um arquivo chamado livros.csv, onde eu irei escrever (w) - isso porque por padrão o python cria um reader e não um writer. Entenda que a nova linha vem em branco (newline = '') e que os dados estarão no formato 'utf-8') como (as) um arquivo csv (csvfile)
    escritor = csv.writer(csvfile) #aqui você cria uma variável escritor e cria um objeto writer que será usado para escrever dados nesse arquivo csv que foi criado acima
    escritor.writerow (['id', 'titulo', 'autor', 'ano', 'preco']) #aqui nessa linha nós vamos pedir para que o escritor escreva uma linha com essas informações (writeROW)
    escritor.writerows(livros) #nessa linha, pedimo que o escritor escreva várias linhas (writeROWS) com as informações que estão lá na lista livros que criamos acima