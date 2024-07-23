#4. **Atualizando Dados**
  # - Escreva um script Python que atualize o preço de um livro específico (por exemplo, mude o preço do livro com `id` 1 para 29.99).

import sqlite3
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (29.99, '1'))

conn.commit()
cursor.close()
conn.close()