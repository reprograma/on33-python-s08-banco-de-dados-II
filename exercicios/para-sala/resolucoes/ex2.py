# Inserção de Dados
import sqlite3

conn = sqlite3.connect('escola.db') #conectar com o banco
cursor = conn.cursor()  # definir o cursor
# Lista de informações 
estudantes = [
       ('Alice', 21),
       ('Bob', 22),
       ('Charlie', 23)
   ]

cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes) # insere mais de uma informação uma única vez

conn.commit()
cursor.close()
conn.close()
