import sqlite3


def createSqlDB():
    conn = sqlite3.connect('mami.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            productCode TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
