# Remoção de Dados para mais de uma opção 
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

estudantes = [
    (4,),
    (5,),
    (7,),
    (8,),
    (10,),
    (11,),
    (13,),
    (14,),
]

cursor.executemany("DELETE FROM estudantes WHERE id = ?", estudantes) # é necessário ter a virgula pois espera-se dois parâmetros ns função

conn.commit()
cursor.close()
conn.close()