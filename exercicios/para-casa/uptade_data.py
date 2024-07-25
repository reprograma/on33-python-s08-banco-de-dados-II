import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def atualizar():
    identificador = input('Digite o ID do livro a ser atualizado: ')
    cursor.execute("SELECT * FROM livros WHERE id = ?", (identificador,))
    livro = cursor.fetchone()

    if livro is None:
        print(f"Erro! Livro com ID {identificador} não encontrado.")
        return

    livroAtual = livro
    print(f'Livro a ser alterado: ID: {livroAtual[0]}, Título: {livroAtual[1]}, Autor: {livroAtual[2]}, Ano: {livroAtual[3]}, Preço atual: R$ {livroAtual[4]:.2f}')

    precoNovo = input('Digite o novo preço separado por ponto, se necessário: ')
    preco = float(precoNovo)
    cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (preco, identificador))
    print('Preço atualizado com sucesso!')

    try:
        if int(identificador) <= 0:
            raise ValueError("ID deve ser maior que zero")
        if preco <= 0:
            raise ValueError("Preço deve ser maior que zero")
    except ValueError as e:
        print(f'Erro: {e}')
    except Exception as e:
        print(f'Erro na atualização de dados. Erro: {e}')

atualizar()

conn.commit()
cursor.close()
conn.close()
