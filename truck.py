
from datetime import datetime, timedelta
class truck:
    def __init__(self,):
        truckNumber = 0
        truckDepartureTime = datetime.today().replace(hour=10, minute=0, second=0, microsecond= 0)
        time = truckDepartureTime
        packages = []
        
        
    def isFull(self):
        if len(self.packages) > 16:
            raise Exception("The truck is overloaded")
        elif len(self.packages) == 16:
            return 1
        else:
            return 0
    def isNotEmpty(self):
        if len(self.packages) > 0:
            return True
        else: False
        
        
    def loadPackage(self, packageID):
        self.packages.append(packageID)
    def unloadPackage(self, packageID):
        self.packages.remove(packageID)
    def addTime(self, minutes):
        self.time = self.time + timedelta(minutes=minutes)
    