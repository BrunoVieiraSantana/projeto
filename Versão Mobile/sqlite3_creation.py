import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE usuarios (
        id_user INTEGER PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        senha VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        status VARCHAR(255) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE fluxo (
        id_fluxo INTEGER PRIMARY KEY,
        tipo VARCHAR(255) NOT NULL DEFAULT '1',
        valor REAL NOT NULL,
        vencimento VARCHAR(10) DEFAULT '1',
        status VARCHAR(255) DEFAULT '0',
        reserva REAL DEFAULT 0,
        id_user INTEGER NOT NULL DEFAULT 1,
        CONSTRAINT fk_user
            FOREIGN KEY(id_user)
            REFERENCES usuarios(id_user)
    )
''')

conn.commit()
conn.close()
