from . import core
import json
class db:
    def insertByType(self, datas):
        self.data = json.loads(datas)

        if self.data['type'] == 'airportInsert':
            self.insertAirportsAndCities()
    def executeCommands(self, commands):
        dbCore = core.core()
        dbCore.executeCommands(commands)
        dbCore.close()
    def executeSelect(self, command):
        dbCore = core.core()
        res = dbCore.executeSelectCommand(command)
        dbCore.close()
        return res
    def insertAirportsAndCities(self):
        self.extractCountries()
        self.regions=self.data['data']['regions']
        self.countries=self.data['data']['countries']
        self.cities = self.data['data']['cities']
        self.airports = self.data['data']['airports']
        self.commands = []
        # commands=self.insertRegions()
        # self.executeCommands(commands)
        commands = self.insertCountries()
        self.executeCommands(commands)
    def extractCountries(self):        
        regions = self.executeSelect('Select \"ID\", \"regionName\" from regions')
        for country in self.data['data']['countries']:
            for region in regions:
                if region[1] == country['region']:
                    country['region'] = region[0]    
    def insertRegions(self, outsource=False, regions=None):        
        if outsource:
            pass
        else:                    
            resCommand =[]
            for region in self.regions:
                resCommand.append(self.createInsertCommand(columns=['regionName'], values=region,table='regions', isRegion=True))
            return resCommand
    def insertCountries(self, outsource=False, countries=None):
        if outsource:
            pass
        else:
            resCommand = []
            for country in self.countries:
                resCommand.append(self.createInsertCommand(columns=['code','name','regionId'],values=[country['code'],country['name'], country['region']], table='countries'))    
            return resCommand
    def insertCities(self, outsource=False, cities=None):
        if outsource:
            pass
        else:
            return self.createInsertCommand(columns=[''], values=self.cities, table='cities')
    def insertAirports(self, outsource=False, airports=None):
        if outsource:
            pass
        else:
            return self.createInsertCommand(columns=[''],values=self.airports, table='airports')
    def createInsertCommand(self,columns, values, table, isRegion=False):
        valuesAsCommand = None
        columnsAsCommand = None
        if isRegion:            
            valuesAsCommand = values
            columnsAsCommand = '\", \"'.join(columns)
            # commandStr = 'Insert Into {0} (\"{1}\") Values(\'{2}\') on conflict do nothing'.format(table, columnsAsCommand, valuesAsCommand)
            # return commandStr
        else:            
            valuesAsCommand = '\', \''.join(str(e) for e in values)
            columnsAsCommand = '\", \"'.join(columns)
        commandStr = 'Insert Into {0} (\"{1}\") Values(\'{2}\') on conflict do nothing'.format(table, columnsAsCommand, valuesAsCommand)
        return commandStr
    def createSelectCommand(self, desiredValues, table, multipleValues=False):
        valuesAsCommand = None
        if multipleValues:
            valuesAsCommand = ''
        commandStr = 'Select '
# print(db.createCommand('self',columns=['deneme1','deneme2','deneme3','deneme4'],values=['deneme1', 2,'deneme3',4.2],table = 'testTablo'))