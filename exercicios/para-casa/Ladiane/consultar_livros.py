#**Consulta de Dados**:
import sqlite3 

# Conecta ao banco de dados SQLite chamado 'livraria.db'
# Se não existir, ele será criado
conn = sqlite3.connect('livraria.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# selecionar todos os registros da tabela 'livros'

cursor.execute("SELECT * FROM livros")


# 'fetchall()' retorna uma lista de tuplas, onde cada tupla representa uma linha da tabela
registros = cursor.fetchall()

# Itera sobre cada registro na lista de registros
# Cada registro é uma tupla contendo os dados de uma linha da tabela
for registro in registros:
    print(registro)  

# Fecha 
cursor.close()
conn.close()


# Tuplas são úteis quando você deseja garantir que os dados não sejam
# alterados após a criação e quando você precisa de uma estrutura de dados 
# que pode ser usada como chave em um dicionário ou que precisa ser garantidamente
# hashable. São amplamente usadas para armazenar dados estruturados e são uma parte
# fundamental da linguagem Python
