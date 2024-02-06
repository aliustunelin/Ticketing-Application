import sqlite3

def updateProduct(productCode, new_quantity):
    conn = sqlite3.connect('mami.db')
    cursor = conn.cursor()

    try:
        
        cursor.execute("SELECT * FROM Products WHERE productCode=?", (productCode,))
        product = cursor.fetchone()

        if product:
            cursor.execute("UPDATE Products SET quantity=? WHERE productCode=?", (new_quantity, productCode))

            conn.commit()
            response = {
                "Status":"Success!"
            }
            return response
        
        else:
            response = {
                "Status":"Unsuccessful!"
            }
            return response
        
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        conn.close()

