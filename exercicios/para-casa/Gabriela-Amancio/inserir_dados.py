import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def inserir():
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o autor do livro: ')
    anoInserido = input('Digite o ano do livro: ')
    precoInserido = input('Digite o preço do livro separado por ponto: ')

    try:
        ano = int(anoInserido)
        preco = float(precoInserido)
        cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (titulo, autor, ano, preco))
        print('Livro inserido com sucesso!')
    except ValueError as e:
        print(f'Erro: {e}')
    except Exception as e:
        print(f'Erro na inserção de dados. Erro: {e}')

inserir()

conn.commit()
cursor.close()
conn.close()