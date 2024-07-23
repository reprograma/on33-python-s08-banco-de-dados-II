import sqlite3  

conn = sqlite3.connect('livraria.db') 
cursor = conn.cursor() 


cursor.execute("UPDATE livros SET Preco = ? WHERE Titulo = ?", (49.90, 'Quem é Você, Alasca?'))


conn.commit()
cursor.close()
conn.close()