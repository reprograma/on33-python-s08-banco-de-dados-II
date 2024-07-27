# 5. **Removendo Dados**
#   - Escreva um script Python que remova um livro específico da tabela (por exemplo, remova o livro com `id` 3).

import sqlite3


def excluir ():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    select_id = input("Digite o id que deseja deletar: ")

    cursor.execute('SELECT * FROM livros WHERE id = ?', (select_id))
    registro = cursor.fetchall()
    print("Tem certeza que deseja deletar o registro abaixo?")
    print(registro)

    opcao = input("Digite sua opção - S: continuar / N: cancelar - : ")

    if opcao.capitalize() == "S":
        cursor.execute('DELETE FROM livros WHERE id = ?', (select_id))
        print("Registro deletado")

    elif opcao.capitalize() == "N":
        print("Fim do programa")

    else:
        print("Você não digitou uma opção válida. Reinicie")
        excluir()

    conn.commit()
    cursor.close
    conn.close

excluir()