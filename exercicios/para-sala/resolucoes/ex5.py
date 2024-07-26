import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM estudantes WHERE id = ?", ('Charlie',))

conn.commit()
cursor.close()
conn.close()