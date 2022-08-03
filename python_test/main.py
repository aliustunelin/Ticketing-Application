import json
from airports import cities
from db import insert
from auth import auth
class search:
    def getToken(self):
        a = auth.authenticate()
        return a.getToken()

    def airPorts(self,link, cityCode):
        tmp = json.loads(cities.getAirports(self.token,link))
        _airports = []
        for port in tmp['Airports']:
            _airports.append({'code':port['code'],'name':port['name']})
        res = {'cityCode':cityCode,'Airports':_airports}
        return res

    def parseCities(self, city):
        data = {}#{'type':'airportInsert','data':{'regions':_regions, 'countries':_countries, 'cities':_cities, 'airports':_airportLinks}}
        with open('parsedData/airportList.json','r') as ww:
            data = ww.read()
            # data = json.loads(d)
        #insrt = insert()
        # print(data)
        insrt = insert.db()
        insrt.insertByType(datas=data)
    def entry(self,request_content):
        self.token = self.getToken()
        tmpJson = json.loads(self.cities.getCities(token))
        self.parseCities(tmpJson['Cities'])
