import distance
from datetime import datetime, timedelta
class truck:
    
    
    def __init__(self,):
        self.truckNumber = 0
        self.truckDepartureTime = datetime.today().replace(hour=0, minute=0, second=0, microsecond= 0)
        self.time = self.truckDepartureTime
        self.packages = []
        self.currentLocation = 'HUB'
        self.distanceTraveled = 0
        
        self.distanceObj = distance.Distance()
        self.distanceObj.loadDistanceTable()
  
    def isFull(self) -> int:
        if len(self.packages) > 16:
            raise Exception("The truck is overloaded")
        elif len(self.packages) == 16:
            return 1
        else:
            return 0
    def isNotEmpty(self) -> bool:
        if len(self.packages) > 0:
            return True
        else: False
    
    def startDeliveryRoute(self) -> tuple:
        # nextPackage = None    
        # nextPackageDistance = float("inf")
        # for package in self.packages:
        #     #print(f'package on current iteration {package}')
        #     currentLocation = self.currentLocation
        #     if  self.distanceObj.returnDistance(self.distanceObj.returnAddressIndex(currentLocation),self.distanceObj.returnAddressIndex(package[1]) ) < nextPackageDistance:
        #         nextPackage = package
        #         nextPackageDistance = self.distanceObj.returnDistance(self.distanceObj.returnAddressIndex(self.currentLocation),self.distanceObj.returnAddressIndex(package[1]) )
        #         print(f'found closer package {package[0]}, at {package[1]}, {nextPackageDistance} away')
            
        while self.isNotEmpty():
            nextPackage, nextPackageDistance = self.distanceObj.nearestNeighbor(self.currentLocation, self.packages)
                
                
            self.addTime(self.distanceObj.calculateTimeGivenDistance(nextPackageDistance))
            self.addDistance(nextPackageDistance)
            print(f'arrived at {nextPackage[1]}, trip took: {self.distanceObj.calculateTimeGivenDistance(nextPackageDistance)} minutes')
            self.currentLocation = nextPackage[1]
            print(f'updating my current location to {nextPackage[1]}')
            self.unloadPackage(nextPackage[0])
            print(f'unloading package ID: {nextPackage[0]}')
            print(f'time is {self.time}')
            
        print(f'All packages delivered, returning to HUB')
        distanceToHUB = self.distanceObj.returnDistance(self.distanceObj.returnAddressIndex(self.currentLocation),self.distanceObj.returnAddressIndex('HUB'))
        self.addDistance(distanceToHUB)
        self.addTime(self.distanceObj.calculateTimeGivenDistance(distanceToHUB))
            

        return self.truckDepartureTime, self.time, self.distanceTraveled
            
        
    def loadPackage(self, packageID, address) -> None:
        self.packages.append((packageID, address))
    def unloadPackage(self, packageID) -> None:
        for package in self.packages:
            if package[0] == packageID:
                self.packages.remove(package)
                break
    def addTime(self, minutes) -> None:
        self.time = self.time + timedelta(minutes=minutes)
    def setCurrentLocation(self,address) -> None:
        self.currentLocation = distance.Distance.returnAddressIndex(address)
        
    def addDistance(self, distance) -> None:
        self.distanceTraveled = self.distanceTraveled + distance    
    
    
    
    def __repr__(self) -> str:
        return f'Packages in this truck: {self.packages} distance traveled: {self.distanceTraveled}'
    

    