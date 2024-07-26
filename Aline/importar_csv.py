import sqlite3
import csv

livros = [
    [1, 'One Piece', 'Eiichiro Oda', 1997, 34.90],
    [2, 'Naruto', 'Masashi Kishimoto', 2002, 29.90],
    [3, 'Attack on Titan', 'Hajime Isayama', 2009, 39.90],
    [4, 'Death Note', 'Tsugumi Ohba', 2003, 24.90],
    [5, 'My Hero Academia', 'Kohei Horikoshi', 2014, 49.90],
    [6, 'Demon Slayer: Kimetsu no Yaiba', 'Koyoharu Gotouge', 2016, 44.90]
]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
       escritor = csv.writer(csvfile)
       escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preço'])
       escritor.writerows(livros)


conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
with open('livros.csv', newline='', encoding='utf-8') as csvfile:
  leitor = csv.reader(csvfile)
  next(leitor)
  for item in leitor:
    cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (item[1], item[2], item [3], item [4]))

conn.commit()
cursor.close()
conn.close()