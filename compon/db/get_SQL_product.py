import sqlite3

def listAllProducts():
    
    conn = sqlite3.connect('mami.db')
    cursor = conn.cursor()

    productList=[]

    try:    
        cursor.execute("SELECT * FROM Products")
        
        rows = cursor.fetchall()
        for row in rows:
            productList.append({
                "ID":row[0],
                "Name":row[1],
                "Product Code":row[2],
                "Quantity" : row[3]
            })

        return productList
        
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        conn.close()

