##1. CRIANDO O BANCO DE DADOS E A TABELA

import sqlite3

#Com a criação da variável abaixo estamos criando um banco de dados chamado "livraria.db" (isso porque esse data base ainda não existe)
conn = sqlite3.connect('livraria.db')

#Com a variável abaixo, estamos criando um cursos, que vai ser o elemento que vai receber comandos
cursor = conn.cursor()


#Agora vamos inserir as informações nesse banco de dados usando os comandos conforme usamos no SQLite, contudo, aqui, temos que dar alguns comandos adicionais por estarmos fazendo isso em Python

#Começamos pedindo para que o cursor execute essa criação, que vai ser delineada por meio de uma string que vai passar os parâmetros de cada campo dessa tabela que será criada.

cursor.execute("""
               CREATE TABLE IF NOT EXISTS livros (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               autor TEXT NOT NULL,
               ano INTEGER,
               preco REAL
               )
               """)
