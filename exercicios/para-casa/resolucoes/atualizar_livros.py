import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

titulo = input("titulo:")
autor = input("autor:")
ano = input("ano:")
preco = input("preco:")
id = input("id:")

cursor.execute("UPDATE livros SET titulo = ?, autor = ?, ano = ?, preco = ? WHERE id = ?", (titulo, autor, ano, preco, id))

conn.commit()
cursor.close()
conn.close()


'''
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

estudantes = [
    (20, 'Alice'),
    (21, 'Bob')

]

cursor.executemany("UPDATE estudantes SET idade = ? WHERE nome = ?", estudantes)

conn.commit()
cursor.close()
conn.close()


'''