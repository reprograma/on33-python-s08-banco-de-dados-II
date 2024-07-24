import sqlite3

try:
    # Tenta criar uma conexão com um banco de dados SQLite em memória.
    conn = sqlite3.connect(':memory:')
    print("O SQLite está funcionando no seu sistema.")
    conn.close()
except sqlite3.Error as e:
    print(f"Erro: {e}")
    print("O SQLite não está funcionando corretamente no seu sistema.")
