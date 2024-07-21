import sqlite3
import csv
livros_ = [
       [1, 'Dom Casmurro', 'Machado de Assis', 1949, 24.50 ],
       [2, 'Memórias Póstumas de Brás Cuba', 'Machado de Assis', 1881, 27.50],
       [3, 'Grande Sertão Veredas', 'João Guimarães Rosa', 1956, 32.00],
       [4, 'Macunaíma', 'Mário de Andrade', 1928, 22.90],
       [5, 'Capitães de Areia', 'Jorge Amado', 1937, 25.00]
   ]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
       escritor = csv.writer(csvfile)
       escritor.writerow(['id', 'título', 'autor', 'ano', 'preço'])
       escritor.writerows(livros_)


conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
with open('livros.csv', newline='', encoding='utf-8') as csvfile:
       leitor = csv.reader(csvfile)
       next(leitor)  # Pular o cabeçalho
       for item in leitor:
           cursor.execute("INSERT INTO livros (título, autor, ano, preço) VALUES (?, ?, ?, ?)", (item[1], item[2], item [3], item [4]))

conn.commit()
cursor.close()
conn.close()