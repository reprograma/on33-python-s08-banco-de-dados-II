import sqlite3

#conexão
conn = sqlite3.connect('livraria.db')

#colocar os comandos sql
cursor = conn.cursor()

#colocar os comandos SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL, 
            ano INTEGER NOT NULL, 
            preco REAL               
)
""")

# commit a informação
conn.commit()
# fechar a conexão
cursor.close()
conn.close()



