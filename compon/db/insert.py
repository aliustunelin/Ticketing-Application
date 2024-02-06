import sqlite3


def insertOneProduct(name, productCode, quantity):

    try:
        conn = sqlite3.connect('mami.db')
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO Products (name, productCode, quantity) VALUES (?, ?, ?)",
                     (name, productCode, quantity))

        conn.commit()

    except Exception as e:
        print(f"Hata: {e}")
        conn.rollback()
    finally:
        conn.close()
    