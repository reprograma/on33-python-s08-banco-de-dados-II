import sqlite3

#conectar ao banco de dados (ou criar um banco de dados)
conexao = sqlite3.connect('livraria.db')
cursor = conexao.cursor() 

#criar a tabela de livros
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
               id INTEGER PRIMARY KEY,
               titulo TEXT NOT NULL,
               autor TEXT NOT NULL,
               ano INTEGER NOT NULL,
               preco REAL NOT NULL
)
""")

conexao.commit()
cursor.close()
conexao.close()