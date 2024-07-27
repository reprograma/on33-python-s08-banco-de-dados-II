# 🏦🎲 Banco de Dados - Integração Completa de CSV com SQLite usando Python

## 📚 Descrição da Atividade

A ideia aqui é praticar como integrar arquivos CSV com um banco de dados SQLite usando Python. Vamos criar um banco de dados, importar dados de um arquivo CSV para uma tabela, fazer operações de CRUD (Create, Read, Update, Delete) e, no final, exportar os dados da tabela para um novo arquivo CSV.

## 📋 Passo a Passo

## 1. **Criando o Banco de Dados e a Tabela**

                import sqlite3
                print(sqlite3.sqlite_version)

                conn = sqlite3.connect('livraria.db')
                cursor = conn.cursor()

                cursor.execute("""
                            CREATE TABLE IF NOT EXISTS livros (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            autor TEXT NOT NULL,
                            ano INTEGER,
                            preco REAL
                            )
                            """)


## 2. **Importando Dados de um CSV**

            import csv

            livros = [
                [1, 'A Invenção do Racismo na Antiguidade', 'Mário Sérgio Conti', 2021, 39.90],
                [2, 'Quarto de Despejo: Diário de uma Favelada', 'Carolina Maria de Jesus', 1960, 29.90],
                [3, 'Pequeno Manual Antirracista', 'Djamila Ribeiro', 2019, 24.90],
                [4, 'Olhares Negros: Raça e Representação', 'Bell Hooks', 1992, 34.90],
                [5, 'Eu Sei Por Que o Pássaro Canta na Gaiola', 'Maya Angelou', 1969, 42.90],
                [6, 'Racismo Estrutural', 'Silvio Almeida', 2019, 36.90],
                [7, 'O Genocídio do Negro Brasileiro', 'Abdias do Nascimento', 1978, 49.90]
            ]

            with open ('livros.csv', 'w', newline='', encoding='utf-8') as csvfile: 
                escritor = csv.writer(csvfile) 
                escritor.writerow (['id', 'titulo', 'autor', 'ano', 'preco']) 
                escritor.writerows(livros) 

## 3. **Consultando e Exibindo Dados**

            import sqlite3

            conn = sqlite3.connect('livraria.db')
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM livros')
            registros = cursor.fetchall()

            for registro in registros:
                print(registro)

            cursor.close
            conn.close

## 4. **Atualizando Dados**

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

## 5. **Removendo Dados**

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

## 6. **Exportando Dados para CSV**

            import sqlite3
            import csv

            conn = sqlite3.connect('livraria.db')
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM livros")
            dados = cursor.fetchall()

            with open ('exportados_livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
                escritor = csv.writer(csvfile)
                escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
                escritor.writerows(dados)

            cursor.close
            conn.close

            print("Dados foram exportados para o arquivo exportados_livros.csv")       


## 👩🏻‍🏫 Profa. Leticia!
Professora [Leticia](https://davinyleticia.bio/)

## 🔚