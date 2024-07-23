import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Lista de estudantes a serem inseridos
estudantes = [
    ('Alice', 21),
    ('Bob', 22),
    ('Charlie', 23)
]

# Inserir os dados na tabela 'estudantes'
cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

# Confirmar a transação
conn.commit()

# Fechar o cursor e a conexão
cursor.close()
conn.close()

