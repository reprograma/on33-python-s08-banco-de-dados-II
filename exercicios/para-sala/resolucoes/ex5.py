# Remoção de Dados
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',)) # é necessário ter a , pois espera-se dois parâmetros ns função

conn.commit()
cursor.close()
conn.close()