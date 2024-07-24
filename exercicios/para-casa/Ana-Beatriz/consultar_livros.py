import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM livros')

dados = cursor.fetchall()

for dado in dados:
    print(dado)
    
cursor.close()
conn.close()
