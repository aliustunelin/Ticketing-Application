from flask import Flask, jsonify
import requests


def getEntegraDataShowJson(token):
    api_url = f"https://apiv2.mami.com/product/page=1/"

    
    headers = {
        'Authorization': f'JWT {token}',
        'Content-Type': 'application/json'
    }


    try:
        response = requests.get(api_url, headers=headers)

        responseProduct = list(map(lambda x:x, response.json()['productList'][:5]))



        returnData = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*', 
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            "Access-Control-Allow-Credentials": True,
            'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                'body': responseProduct
            } 

        return returnData


    except FileNotFoundError:
        return jsonify(error="your credentials request not working!"), 404

