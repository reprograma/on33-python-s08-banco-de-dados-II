import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Encontrar IDs de livros duplicados mantendo o primeiro
cursor.execute("""
    WITH Duplicates AS (
        SELECT MIN(id) AS keep_id
        FROM livros
        GROUP BY titulo, autor, ano, preco
        HAVING COUNT(*) > 1
    )
    DELETE FROM livros
    WHERE id NOT IN (SELECT keep_id FROM Duplicates)
    AND (titulo, autor, ano, preco) IN (
        SELECT titulo, autor, ano, preco
        FROM livros
        GROUP BY titulo, autor, ano, preco
        HAVING COUNT(*) > 1
    )
""")

# Confirmar a remoção
conn.commit()

# Exibir mensagem de sucesso
print("Livros duplicados foram removidos com sucesso.")

# Fechar a conexão
cursor.close()
conn.close()
