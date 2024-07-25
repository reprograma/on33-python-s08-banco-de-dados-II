import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def remover():
    identificador = input('Digite o ID do livro a ser removido: ')
    cursor.execute("SELECT * FROM livros WHERE id = ?", (identificador,))
    livro = cursor.fetchone()

    if livro is None:
        print(f"Erro! Livro com ID {identificador} não encontrado.")
        return

    livroAtual = livro
    print(f'Livro a ser excluído: ID: {livroAtual[0]}, Título: {livroAtual[1]}, Autor: {livroAtual[2]}, Ano: {livroAtual[3]}, Preço atual: R$ {livroAtual[4]:.2f}')

    confirma = input('Deseja excluir este livro? (S/N): ')
    if "S" in confirma.upper():
        cursor.execute("DELETE FROM livros WHERE id = ?", (identificador,))
        print('Livro excluído com sucesso!')
    else:
        print('Exclusão cancelada.')

    try:
        if int(identificador) <= 0:
            raise ValueError("ID deve ser maior que zero")
    except ValueError as e:
        print(f'Erro: {e}')
    except Exception as e:
        print(f'Erro na exclusão de dados. Erro: {e}')

remover()

conn.commit()
cursor.close()
conn.close()
