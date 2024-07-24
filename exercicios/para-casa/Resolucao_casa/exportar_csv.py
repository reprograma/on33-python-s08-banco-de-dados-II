import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()


cursor.execute("SELECT * FROM livros")
livros = cursor.fetchall()

csv_file = 'exportados_livros.csv'


cursor.execute("PRAGMA table_info(livros)")
colunas = [col[1] for col in cursor.fetchall()]


with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(colunas)  # Escrever o cabeçalho
    writer.writerows(livros)  # Escrever os dados
