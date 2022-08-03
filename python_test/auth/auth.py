import requests
import json
import datetime

base_url ='https://api.iata.org' 
url_ext = '/v2/identity.mozilla.com/picl/v1/sessionToken'
class authenticate:
    def getToken(self):
        localData = {}
        with open('./auth/auth.txt','r') as rr:
            localData = rr.read()
        res = ''
        localData = json.loads(localData)
        if 'error' not in localData:
            if self.expirationControl(localData['expires']):            
                res = localData['token']
                print(localData['expires'])
            else:
                requestedData = self.request()
                res = 'hawk_session '+requestedData['access_token']
                expires_in = requestedData['expires_in']
                self.writeOut(res,expires_in)            
            return 200, res
        else:
            return 1001, res
    def expirationControl(self, expires):
        now = datetime.datetime.now()
        if now.timestamp() < expires:
            return True
        else:
            return False
    def request(self):
        url=base_url+url_ext
        headers = {
            'Authorization': 'Basic VmpFNllYWmhkM05yT0dacVpHNDVZV1JyYWpwRVJWWkRSVTVVUlZJNlJWaFU6ZDJ4TGQxUTVNRW89',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers)
        myData = response.text
        myData = json.loads(myData)
        response.close()
        return myData
    def writeOut(self, token, expirationSeconds):
        expires = datetime.datetime.now() + datetime.timedelta(seconds=expirationSeconds)        
        output = {'token':token,'expires':expires.timestamp()}
        print(output)
        with open('./auth/auth.txt', 'w') as jw:        
            json.dump(output, jw)

# au = authenticate()
# print(au.getToken())