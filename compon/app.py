from flask import Flask, jsonify, request
import requests
import json
import sqlite3
from compon.products import get_data_From_en

from products import get_all_data

from configs import setup

from auth import auth

from db import insert, search, update , get_SQL_product, delete


app = Flask(__name__)
database_setup_done = False

def setup_database():
    setup.createSqlDB()
    
    myNewToken =  auth.getAllToken()
    productListFrom = get_all_data.getGeneralData(myNewToken)
    for ctx in productListFrom:
        name = str(ctx['name'])
        productCode = str(ctx['productCode'])
        quantity = int(ctx['quantity'])
        insert.insertOneProduct(name=name, productCode=productCode, quantity=quantity)



# no one more time running just run start the app 
@app.before_request
def before_first_request():
    global database_setup_done

    if not database_setup_done:
        setup_database()
        database_setup_done = True


# response all data from SQL so first 5 data all of them
@app.route('/api/data', methods=['GET'])
def get_data_to_SQL():

    response = get_SQL_product.listAllProducts()
    return {
        "Products": response
    }


# search by productCOde and return data infos from sql tables
@app.route('/api/product/search', methods=['POST'])
def search_data():
    reqData = request.get_json()
    productCode = str(reqData['productCode'])
    response = search.findByProductCode(productCode=productCode)

    return {
        "Search" : response
    }



@app.route('/api/product/update', methods=['POST'])
def update_data():
    reqData = request.get_json()
    productCode = str(reqData['productCode'])
    quantity = int(reqData['quantity'])
    response = update.updateProduct(productCode=productCode, new_quantity=quantity)

    return {
        "Update": response
    }


@app.route('/api/product/delete', methods=['POST'])
def delete_data():
    reqData = request.get_json()
    productCode = str(reqData['productCode'])
    response = delete.deleteProduct(productCode=productCode)

    return {
        "Delete": response
    }


# if u want see your GetProducts apis response datas with json
@app.route('/api/data/from_entegra', methods=['GET'])
def get_data():
    myNewToken =  auth.getAllToken()
    product = get_data_From_en.getEntDataShowJson(myNewToken)
    return product



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run(debug=True)
