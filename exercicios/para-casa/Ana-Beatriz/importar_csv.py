
import csv

livros = [
    ["A República", "Platão", "380 a.C.", 49.99],
    ["Crítica da Razão Pura", "Immanuel Kant", 1781, 59.90],
    ["Assim Falou Zaratustra", "Friedrich Nietzsche", 1883, 39.50],
    ["O Ser e o Nada", "Jean-Paul Sartre", 1943, 44.00],
    ["Meditações", "René Descartes", 1641, 34.90]
]

with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
       escritor = csv.writer(csvfile)
       escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
       escritor.writerows(livros)
