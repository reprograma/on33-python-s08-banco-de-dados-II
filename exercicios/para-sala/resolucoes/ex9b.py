# Remoção de Dados para mais de uma opção 
import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

clientes = [
    (6,),
    (7,),
    (8,),
    (9,),
    (10,),
]

cursor.executemany("DELETE FROM clientes WHERE id = ?", clientes) # é necessário ter a virgula pois espera-se dois parâmetros ns função

conn.commit()
cursor.close()
conn.close()