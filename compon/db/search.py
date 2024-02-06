import sqlite3



def findByProductCode(productCode):
    conn = sqlite3.connect('mami.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Products WHERE productCode=?", (productCode,))
    
    searchTemp = cursor.fetchall()

    if len(searchTemp) == 0:
        return "There is no match!!"

    productSearchList=[]

    for row in searchTemp:
        productSearchList.append({
            "ID":row[0],
            "Name":row[1],
            "Product Code":row[2],
            "Quantity" : row[3]
        })

    return productSearchList

    # Bağlantıyı kapat
    conn.close()
