
class price:
    # rawData is ItineraryGroups which is a json array
    def getPrice(self, rawData):
        self.rawData = rawData
        _i = []
        for itineraries in rawData['itineraryGroups']:
            _i.append(self.extractItineraries(itineraries))
        result = {'itineraries':_i}        
        return result
    def extractItineraries(self, itineraries):        
        res = []
        for itinerary in itineraries['itineraries']:
            data = {
                'id':itinerary['id'],
                'legs':itinerary['legs'],
                'pricingSource':itinerary['pricingSource'],
                'pricingInformation':self.extractPricing(itinerary['pricingInformation'])
            }
            res.append(data)
        
        defaults = itineraries['groupDescription']['legDescriptions'][0]
        
        result = {
            'departureDate':defaults['departureDate'],
            'departureLocation':defaults['departureLocation'], 
            'arrivalLocation':defaults['arrivalLocation'],
            'itineraries':res
        }
        return result
    def extractPricing(self, pricingRaw):
        result = []
        for pricing in pricingRaw:
            fare = pricing['fare']
            data = {
                'validatingCarrierCode':fare['validatingCarrierCode'],
                'eTicketable':fare['eTicketable'],
                'governingCarriers':fare['governingCarriers'],
                'passengerBasedPricing':self.extractPassengers(fare['passengerInfoList']),
                'baseFare':fare['totalFare']['baseFareAmount'],
                'taxAmount':fare['totalFare']['totalTaxAmount'],
                'totalPrice':fare['totalFare']['totalPrice'],
                'currency':fare['totalFare']['currency']
            }
            result.append(data)
        return result
    def extractPassengers(self, passengerRaw):
        result = []
        for passenger in passengerRaw:
            info = passenger['passengerInfo']
            taxes=[]
            taxSummaries = []
            baggageInformation = {}
            if 'taxes' in info:
                taxes = info['taxes']
            if 'taxSummaries' in info:
                taxSummaries = info['taxSummaries']
            if 'baggageInformation' in info:
                baggageInformation = info['baggageInformation']

            data = {
                'passengerType':info['passengerType'],
                'passengerNumber':info['passengerNumber'],
                'nonRefundable':info['nonRefundable'],
                'fareComponents':info['fareComponents'],
                'taxes':taxes,
                'taxSummaries':taxSummaries,
                'passengerTotalFare':
                {
                    'baseFare':info['passengerTotalFare']['baseFareAmount'],
                    'taxAmount':info['passengerTotalFare']['totalTaxAmount'],
                    'totalFare':info['passengerTotalFare']['totalFare'],
                    'currency':info['passengerTotalFare']['currency']
                },
                'baggageInformation':baggageInformation
            }          
            result.append(data)
        return result