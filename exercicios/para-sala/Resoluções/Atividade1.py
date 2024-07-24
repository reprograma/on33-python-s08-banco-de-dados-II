import sqlite3

conn = sqlite3.connect('escola.db') # coneção com o arquivo escola.db
cursor = conn.cursor() #cursor de mouse

cursor.execute("""
   CREATE TABLE IF NOT EXISTS estudantes (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
       idade INTEGER NOT NULL
   )
   """) # criação da tabela

conn.commit() # para a informação ser guardada
cursor.close() # fechar a conexãio
conn.close() #