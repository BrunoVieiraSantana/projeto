import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM usuarios')

rows = cursor.fetchall()

for row in rows:
    id_user = row[0]
    nome = row[1]
    senha = row[2]
    email = row[3]
    status = row[4]
    print(f"ID: {id_user}, Nome: {nome}, Senha: {senha}, Email: {email}, Status: {status}")

conn.close()
