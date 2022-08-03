import json

class concentrate:
    def init(self, flights, prices, baggageAllowance):
        self.flights = flights
        self.prices = prices
        self.baggageAllowance = baggageAllowance
        data = self.findRelation()
        with open('parsedData/relations.json','w') as ww:
            json.dump(data, ww)
        self.makeRelations(data)
        with open('parsedData/Maderelations.json','w') as ww:
            json.dump(self.flights, ww)  
    def findRelation(self):  
        relations = []  
        for itinerary in self.prices['itineraries']:
            for price in itinerary['itineraries']:
                for connection in self.flights['connections']:
                    for leg in price['legs']:
                        if connection['ref'] == leg['ref']:
                            relations.append({'flightRef': connection['ref'], 'flightType':'connection','priceDetails':price})
                for direct in self.flights['directs']:
                    for leg in price['legs']:
                        if direct['ref'] == leg['ref']:
                            relations.append({'flightRef': direct['ref'], 'flightType':'direct','priceDetails':price})
        return relations
    def makeRelations(self, relations):
        for flight in self.flights['connections']:
            resF, resB = self.relationIterator(flight,relations)
            if resF != 1005:
                flight['prices']=resF
                flight['baggageInformation'] = resB
        for flight in self.flights['directs']:
            resF, resB = self.relationIterator(flight,relations)
            if resF != 1005:
                flight['prices']=resF
                flight['baggageInformatio'] = resB
    def relationIterator(self, flight, relations):
        try:
            bL = []
            for relation in relations:
                if flight['ref'] == relation['flightRef']:
                    rL = []
                    for pricingInformation in relation['priceDetails']['pricingInformation']:  
                        dL = []
                        for pricingInfo in pricingInformation['passengerBasedPricing']:
                            sL = []                      
                            for fares in pricingInfo['fareComponents']:                                
                                for segments in fares['segments']:
                                    mealCode = ''
                                    if 'mealCode' in segments['segment']:                                        
                                        mealCode = segments['segment']['mealCode']
                                    else:
                                        mealCode = 'N'                                        
                                    ss = {
                                        'bookingCode':segments['segment']['bookingCode'],
                                        'cabinCode':segments['segment']['cabinCode'],
                                        'mealCode':mealCode,
                                        'seatsAvailable':segments['segment']['seatsAvailable']
                                    }
                                    sL.append(ss)
                            for baggage in pricingInfo['baggageInformation']:                            
                                bs = {}
                                for baggageDesc in self.baggageAllowance:
                                    if baggage['allowance']['ref'] == baggageDesc['id']:
                                        if 'weight' in baggageDesc:
                                            bs['weight'] = baggageDesc['weight']
                                        if 'unit' in baggageDesc:
                                            bs['unit'] = baggageDesc['unit']
                                        if 'pieceCount' in baggageDesc:
                                            bs['pieceCount'] = baggageDesc['pieceCount']
                                bL.append(bs)
                            dd = {
                                'passengerType': pricingInfo['passengerType'],
                                'passengerCount':pricingInfo['passengerNumber'],
                                'nonRefundable':pricingInfo['nonRefundable'],
                                'passengerBaseFare':pricingInfo['passengerTotalFare']['baseFare'],
                                'passengerTax':pricingInfo['passengerTotalFare']['taxAmount'],
                                'passengerTotalFare':pricingInfo['passengerTotalFare']['totalFare'],
                                'passengerFareComponents':sL,
                                'baggageInformation':bL
                            }                            
                            dL.append(dd)
                        rr = {
                            'baseFare':pricingInformation['baseFare'],
                            'taxAmount':pricingInformation['taxAmount'],
                            'totalPrice':pricingInformation['totalPrice'],
                            'currency':pricingInformation['currency'],
                            'passengerPricing':dL
                        }
                        rL.append(rr)
                    return rL, bL
        except Exception as ex:
            print(str(ex))
        return 1005, 'Something Happened In concentrator. But I have no clue!!'