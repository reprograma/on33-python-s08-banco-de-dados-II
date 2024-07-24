import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def atualizar():
    identificador = input('Digite o ID do livro a ser atualizado: ')
    cursor.execute("SELECT * FROM livros WHERE id = ?", identificador)
    livro = cursor.fetchone()

    id = int(identificador)

    if livro is None:
        print(f"Erro! Livro com ID {identificador} não encontrado.")
        return

    livroAtual = livro
    print(f'Livro a ser alterado: ID: {livroAtual[0]}, Título: {livroAtual[1]}, Autor: {livroAtual[2]}, Ano: {livroAtual[3]}, Preço aual: R$ {livroAtual[4]:.2f}')

    print('\nO que deseja atualizar?')
    print('Digite T para título.')
    print('Digite AU para autor.')
    print('Digite A para ano.')
    print('Digite P para preço.')
    opcao = input('Digite a opção desejada: ').upper()

    if opcao == 'T':
        titulo = input('Digite o novo título do livro: ')
        cursor.execute("UPDATE livros SET titulo = ? WHERE id = ?", (titulo, id))
        print('Título atualizado com sucesso!')
    if opcao == 'AU':
        autor = input('Digite o novo nome do autor: ')
        cursor.execute("UPDATE livros SET autor = ? WHERE id = ?", (autor, id))
        print('Autor atualizado com sucesso!')
    if opcao == 'A':
        anoNovo = input('Digite o novo ano: ')
        ano = int(anoNovo)
        cursor.execute("UPDATE livros SET ano = ? WHERE id = ?", (ano, id))
        print('Ano atualizado com sucesso!')
    if opcao == 'P':
        precoNovo = input('Digite o novo preço separado por ponto, se necessário: ')
        preco = float(precoNovo)
        cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (preco, id))
        print('Preço atualizado com sucesso!')

    try:
        if id <=0:
            raise ValueError ("ID deve ser maior que zero")
        if opcao == 'P' and preco <= 0:
            raise ValueError ("Preço deve ser maior que zero")
        if opcao not in ['T', 'AU', 'A', 'P']:
            print('Digite uma opção válida')
    except ValueError as e:
        print(f'Erro: {e}')
    except Exception as e:
        print(f'Erro na atualização de dados. Erro: {e}')

atualizar()

conn.commit()
cursor.close()
conn.close()