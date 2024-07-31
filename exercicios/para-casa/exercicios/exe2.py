import sqlite3
import csv

livros = [
       [1, 'Teologia Umbandista: Cosmologia E Física Da Alta Energia,', 'Mestre Aramaty', '2001', '23.15'],
       [2, 'Eras - Despertar Livro 1', 'Stephen Play', '2010', '14.90'],
       [3, 'Seja egoísta com sua carreira', 'Luciano Santos', '2021', '45.33'],
       [4, 'Harry Potter e a Pedra Filosofal', 'J.K. Rowling', '2015', '40'],
       [5, 'The Hobbit', 'John Ronald Reuel Tolkien', '1937', '44.56'],
       [6, 'Os miseráveis', 'Victor Hugo', '1862', '111.93']
   ]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor','ano', 'preco'])
    escritor.writerows(livros)

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
with open('livros.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # Pular o cabeçalho
    for item in leitor:
        cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (item[1], item[2], item [3], item [4]))

conn.commit()
cursor.close()
conn.close()