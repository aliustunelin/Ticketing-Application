import requests
import json
class req:
   # base_url = 'https://api.duffel.com/air/orders'

    def getFlight(self, passengers, seats, departure, arrival, departureDate, directOnly, token):        
        data = {
            'OTA_AirLowFareSearchRQ':
            {
                'DirectFlightsOnly':directOnly,
                'OriginDestinationInformation':
                [
                    {
                        'DepartureDateTime':departureDate,
                        'DestinationLocation':
                        {
                            'LocationCode':arrival
                        },'OriginLocation':
                        {
                            'LocationCode':departure
                        },
                        'RPH':'0'
                    }
                ],
                'POS':
                {
                    'Source':
                    [
                        {
                            'PseudoCityCode':'F9CE',
                            'RequestorID':
                            {
                                'CompanyName':
                                {
                                    'Code':'TN'
                                },
                                'ID':'1',
                                'Type':'1'
                            }
                        }
                    ]
                },
                'TPA_Extensions':
                {
                    'IntelliSellTransaction':
                    {
                        'RequestType':
                        {
                            'Name':'50ITINS'
                        }
                    }
                },
                'TravelPreferences':
                {
                    'TPA_Extensions':
                    {
                        'DataSources':
                        {
                            'ATPCO':'Enable',
                            'LCC':'Disable',
                            'NDC':'Disable'
                        },
                        'NumTrips':{}
                    }
                },
                'TravelerInfoSummary':
                {
                    'AirTravelerAvail':
                    [
                        {
                            'PassengerTypeQuantity': passengers
                        }
                    ],
                    'SeatsRequested':seats
                },
                'Version':'2'
            }
        }
        print(json.dumps(data))
        
        return self.bargain(token, json.dumps(data))
    def request(self, headers, url, data='{}'):        
        print('Request Is Being Sent!')
        response = requests.request("POST", url, headers=headers, data=data)
        print('We Have A Response ')
        res = response.text
        resCode = response.status_code
        response.close()
        with open('raw_bargain_data.json', 'w') as rbw:
            rbw.write(res)
        result = json.loads(res)
        if resCode == 200:
            if result['groupedItineraryResponse']['statistics']['itineraryCount'] > 0:
                return 200, result
            else:
                msg =[]
                for message in result['groupedItineraryResponse']['messages']:
                    if message['code'] == 'MSG' or message['code'] == 'PROCESS' or message['code'] == 'ERR':
                        msg.append(message['text'])
                return 1006, {'message':'No Results Found For Specifications', 'details':msg}
        else:
            return 1002, {'message':resCode, 'details':result}
    def bargain(self,token,data):
        url = 'https://api.duffel.com/air/offer_requests?return_offers=false'
        authHeader = {'Authorization':token}
        print('Authorized!')
        return self.request(headers=authHeader,url=url, data=data)