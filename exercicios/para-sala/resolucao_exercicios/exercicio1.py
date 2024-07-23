import sqlite3

conn = sqlite3.connect('escola.db') #cria uma variável para fazer a conexão. Aqui está criando um banco de dados
cursor = conn.cursor() #aqui cria uma variável que é o cursor (um negócio que fica esperando comandos)

#aqui eu estou pedindo pro cursor executar uma coisa, que é Crie um tabela com essas informações aqui: se não existir ainda com esse nome, coloque o nome estudantes. Aí fazemos a mesma coisa que fazíamos lá no Sqlite do site que é criando a tabela, colocando um campo id, um campo nome e um campo idade.
#Essas 3 aspas aqui são a forma padrão de digitar. 
cursor.execute("""
               CREATE TABLE IF NOT EXISTS estudantes(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL
               )
               """)

#depois de criar essa tabela a gente fecha os parênteses.
#abaixo damos o comando para o conn fazer esse commit (subir essas atualização) e depois fecho o cursor e fecho o conn.

conn.commit()
cursor.close()
conn.close()
