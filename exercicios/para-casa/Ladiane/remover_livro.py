import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
# Lista de IDs dos livros a serem removidos
livros = [
    (1,),
    (3,)

]

# Executar a instrução DELETE para cada ID na lista
cursor.executemany("""DELETE FROM livros WHERE id = ?""", livros)

# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()

