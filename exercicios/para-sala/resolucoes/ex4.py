# Atualização de Dados

import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob')) # irá alterar a idade do Bob, foi digitado dois parâmetros,UPDATE/WHERE e (2.Bob)
# caso queira mais de uma informação escreva crsor.executemany

conn.commit() # Necessário pois foi feito ma alteração
cursor.close()
conn.close()