import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("UPDATE livros SET id = ? WHERE preco = ?", (1, 70.33)) 

conn.commit() 
cursor.close()
conn.close()