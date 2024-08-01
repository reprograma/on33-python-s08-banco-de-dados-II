import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

estudantes = [
    (1, id),
    (2, id)
]
cursor.execute("DELETE FROM estudantes WHERE nome = ?", estudantes)

conn.commit()
cursor.close()
conn.close()

