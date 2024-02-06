import sqlite3

def deleteProduct(productCode):
    conn = sqlite3.connect('mami.db')
    cursor = conn.cursor()

    try:
        
        cursor.execute("DELETE FROM Products WHERE productCode=?", (productCode,))
        conn.commit()
        conn.close()
        return {
            "Status":"Success!"
        }

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
