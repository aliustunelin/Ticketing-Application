from flask import Flask, jsonify
import json
import requests

#credentials
# This is Entegra GET Credentials public url 

BASE_HOST = "https://apiv2.mami.com"
ConrollerName ="product"
EndpointName ="page=1/"

def getGeneralData(token):

    url = f"{BASE_HOST}/{ConrollerName}/{EndpointName}"
    
    headers = {
        'Authorization': f'JWT {token}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(url, headers=headers)
        responseProduct = list(map(lambda x:x, response.json()['productList'][:5]))

        return responseProduct

    except FileNotFoundError:
        return jsonify(error="your product request not working!"), 404

