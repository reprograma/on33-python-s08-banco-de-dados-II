# 4. **Atualizando Dados**
#   - Escreva um script Python que atualize o preço de um livro específico (por exemplo, mude o preço do livro com `id` 1 para 29.99).#

import sqlite3

def atualizar ():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    select_id = input("Digite o id do livro que deseja alterar o preço: ")
    indique_preco = input("Digite o novo preco: ")

    cursor.execute('UPDATE livros SET preco = ? WHERE id = ?', (indique_preco, select_id))

    conn.commit()

    cursor.execute('SELECT * FROM livros WHERE id = ?', (select_id))
    registro = cursor.fetchall()

    print(f"Os dados do livro abaixo foram atualizado com o novo preço de {indique_preco}")
    print(registro)


    cursor.close
    conn.close

atualizar()