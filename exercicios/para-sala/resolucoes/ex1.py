# Criação de Banco de Dados e Tabelas
import sqlite3

conn = sqlite3.connect('escola.db') # conecta o sqlite ao banco de dados criado, esta informação está na varável conn (conexão).
cursor = conn.cursor() # cursor é ma função

# o AUTOINCREMENTE faz com que o programa numere as linhas automaticamente.
# NOT NULL: não permite que na colna criada tenha algo zerado, ela é forçada a escrever algo
# NOT EXISTS: indica neste caso que se a tabela estudante já existe, não dar continuidade aos outros comandos.
 
cursor.execute("""
   CREATE TABLE IF NOT EXISTS estudantes (
       id INTEGER PRIMARY KEY AUTOINCREMENT, 
       nome TEXT NOT NULL,
       idade INTEGER NOT NULL
   )
   """)

conn.commit() # sempre qe fizer uma alteração na tabela, deve comitar para atualizar
cursor.close() # fecha o cursor
conn.close() # fecha a conexão, não deve ficar aberto.
  