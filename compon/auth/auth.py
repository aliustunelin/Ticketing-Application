from flask import Flask, jsonify
import json
import requests

#credentials
# This is mamimami GET Credentials public url 

BASE_HOST = "https://apiv2.***.com"
ConrollerName ="api/user"
EndpointName ="token/obtain/"


def getAllToken():
    
    url = f"{BASE_HOST}/{ConrollerName}/{EndpointName}"
    
    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
     "email": "apiis@***.com",
     "password":"test123."
    }

    try:
        json_payload = json.dumps(payload)
        response = requests.post(url, data=json_payload, headers=headers)
        responseToken = response.json()['access']
        return responseToken

    except FileNotFoundError:
        return jsonify(error="your credentials request not working!"), 404

