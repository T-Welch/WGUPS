import distance
from datetime import datetime, timedelta
class truck:
    
    
    def __init__(self,):
        self.truckNumber = 0
        self.truckDepartureTime = datetime.today().replace(hour=10, minute=0, second=0, microsecond= 0)
        self.time = self.truckDepartureTime
        self.packages = []
        self.currentLocation = "HUB"
        
        self.distanceObj = distance.Distance()
        self.distanceObj.loadDistanceTable()
  
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
    
    def startDeliveryRoute(self):
        nextPackage = None    
        nextPackageDistance = float("inf")
        for package in self.packages:
            print(f'package on current iteration {package}')
            currentLocation = self.currentLocation
            if   self.distanceObj.returnDistance(self.distanceObj.returnAddressIndex(currentLocation),self.distanceObj.returnAddressIndex(package[1]) ) < nextPackageDistance:
                nextPackage = package
                nextPackageDistance = self.distanceObj.returnDistance(self.distanceObj.returnAddressIndex(self.currentLocation),self.distanceObj.returnAddressIndex(package[1]) )
                print(f'found closer package {package[0]}, at {package[1]}, {nextPackageDistance} away')
        
    def loadPackage(self, packageID, address):
        self.packages.append((packageID, address))
    def unloadPackage(self, packageID):
        for package in self.packages:
            if package[0] == packageID:
                self.packages.remove(package)
                break
    def addTime(self, minutes):
        self.time = self.time + timedelta(minutes=minutes)
    def setCurrentLocation(self,address):
        self.currentLocation = distance.Distance.returnAddressIndex(address)
        
    def __repr__(self) -> str:
        return f'Packages in this truck: {self.packages}'
    

    