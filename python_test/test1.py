import json
import connectedFlights as cF
import prices as prc
import bargainSearch 
from auth import auth
from datetime import datetime
import concentrateFlights as concentrateF
class searcher:
    def getToken(self):
        a = auth.authenticate()
        return a.getToken()
    def getData(self, cont):
        code, token = self.getToken()
        if code == 200:
            bargainer = bargainSearch.req() 
            return bargainer.getFlight(
                passengers=cont['passengers'],
                seats=cont['seats'],
                departure=cont['departure'],
                arrival=cont['arrival'],
                departureDate=cont['departureDate'],
                directOnly=cont['directOnly'], 
                token=token
                )
        else:
            return code, token
    def main(self, requestContent):
        try:
            content = json.loads(requestContent)
            resCode, result = self.getData(content)
            if resCode == 200:
                jsonObj = result
                if 'errorCode' not in jsonObj:
                    # for message in jsonObj['groupedItineraryResponse']['messages']:
                    #     if message['severity'] == 'Error':
                    #         return 1002, jsonObj
                    with open('parsedData/rawData.json', 'w') as jw:
                        json.dump(jsonObj, jw)
                    connected = cF.connectedFlights()
                    connCode, flights = connected.getConnections(jsonObj['groupedItineraryResponse']['scheduleDescs'],jsonObj['groupedItineraryResponse']['legDescs'])
                    if connCode == 200:
                        pc = prc.price() 
                        prices = pc.getPrice(jsonObj['groupedItineraryResponse'])
                        data = {'flights':flights}
                        concetrater = concentrateF.concentrate()
                        concetrater.init(flights, prices, jsonObj['groupedItineraryResponse']['baggageAllowanceDescs'])
                        with open('parsedData/'+str(datetime.now())+'.json', 'w') as jw:
                            json.dump(data, jw)
                        return 200, data
                    else:
                        return connCode, flights
                else:
                    return 1003, jsonObj
            else:
                return resCode, result
        except Exception as ex:
            return 1000, str(ex)

# bg = searcher()
# print(bg.main('{"passengers":[{"Code":"ADT","Quantity":1}],"seats":[1],"departure": "IST","arrival": "DOH","departureDate":"2021-05-15T00:00:00","directOnly": false}'))
