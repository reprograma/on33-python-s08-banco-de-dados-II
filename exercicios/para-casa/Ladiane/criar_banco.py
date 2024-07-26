# **Criação de Banco de Dados e Tabelas**:
import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('livraria.db')
# Criar um cursor para executar comandos SQL
cursor = conn.cursor() # atraves do curso vamos usar  o metodo execute, curso espera uma informação de entrada
# varias """ qundo para executar mais de uma linha "
# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       titulo TEXT NOT NULL,
       autor TEXT NOT NULL,
       ano INTEGER NOT NULL,                           
       preco REAL NOT NULL
   )
   """)
# Confirmar as alterações e fechar a conexão
conn.commit()  # commit igual  do git hub
cursor.close() # fecha
conn.close()  # fechar conexão
# not exists verifica se a tabela existe , caso tenha não fazer novamente
# autoincrement para colocar os números na ordem
# o null para não deixa a linha nulo e  obrigar a a colocar valor 
print("Banco de dados e tabela criados com sucesso!")



