#3. **Consultando e Exibindo Dados**
#   - Escreva um script Python que selecione e exiba todos os registros da tabela `livros`.#
#esse script Python permite a seleção e a exibição de todos os registros da tabela livros, contida no banco de dados livraria

import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM livros')
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close
conn.close