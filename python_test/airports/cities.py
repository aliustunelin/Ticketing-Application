import requests

base_url = 'https://test.api.amadeus.com/v1'

def request(headers, url, data='{}'):        
    response = requests.request("GET", url, headers=headers, data=data)
    res = response.text
    response.close()
    return res
def getCities(token):
    url = base_url+'/airport/direct-destinations'
    authHeader = {'Authorization':token}
    return request(headers=authHeader,url=url)

def getAirports(token,link):
    authHeader = {'Authorization':token}
    return request(url = link, headers=authHeader)
