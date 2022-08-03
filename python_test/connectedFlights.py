import json
class connectedFlights:
    def getConnections(self, allFlights, connections):
        try:
            connectionList = []
            connectedFlights = [] 
            directFlights = []   
            for connection in connections:
                tmpList = []
                for schedules in connection['schedules']:
                    if 'departureDateAdjustment' in schedules:
                        tmpList.append({'ref':schedules['ref'],'departureDateAdjustment':schedules['departureDateAdjustment']})
                    else:
                        tmpList.append({'ref':schedules['ref']})
                # print(len(tmpList))
                if len(tmpList) > 1:
                    paired = []
                    paired = self._pair(allFlights, tmpList)
                    connectedFlights.append({'totalTime':connection['elapsedTime'],'ref':connection['id'],'flight':paired})
                else:
                    for flight in allFlights:
                        if flight['id'] == tmpList[0]['ref']:
                            directFlights.append({'totalTime':connection['elapsedTime'],'ref':connection['id'],'flight':flight})
            result = {'connections':connectedFlights, 'directs':directFlights}
            with open('parsedData/connections.json', 'w') as jw:
                json.dump(result, jw)
            return 200, result
        except Exception as ex:
            return 1004, ex
    def _pair(self, allFlights, connection, departureDateAdjustment = 0):
        connectedFlights = []
        for conn in connection:
            for flight in allFlights:
                if conn['ref'] == flight['id']:       
                    if 'departureDateAdjustment' in conn:
                        flight['departureDateAdjustment'] = conn['departureDateAdjustment']         
                    connectedFlights.append(flight)
        return connectedFlights