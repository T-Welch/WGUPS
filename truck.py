import distance
from datetime import datetime, timedelta
class truck:
    
    
    def __init__(self):
        self.truckNumber = 0
        self.truckDepartureTime = datetime.today().replace(hour=0, minute=0, second=0)
        self.time = self.truckDepartureTime
        self.packages = []
        self.currentLocation = 'HUB'
        self.distanceTraveled = 0
        
        self.distanceObj = distance.Distance()
        self.distanceObj.loadDistanceTable()
        
    def setTime(self, time):
        self.time = time
  
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
    
    def startDeliveryRoute(self, packageManager, packageHashTable) -> tuple:            
        while self.isNotEmpty():
            nextPackage, nextPackageDistance = self.distanceObj.nearestNeighbor(self.currentLocation, self.packages)
                
                
            self.addTime(self.distanceObj.calculateTimeGivenDistance(nextPackageDistance))
            self.addDistance(nextPackageDistance)
            #print(f'arrived at {nextPackage[1]}, trip took: {self.distanceObj.calculateTimeGivenDistance(nextPackageDistance)} minutes')
            self.currentLocation = nextPackage[1]
            #print(f'updating my current location to {nextPackage[1]}')
            packageHashTable[nextPackage[0]].setDeliveryStatus('Delivered')
            packageHashTable[nextPackage[0]].setDeliveryTime(self.time.strftime("%H:%M:%S"))
            key = self.time.strftime("%H:%M:%S")
            packageManager.addToTimeTable(key, packageHashTable)
            #print(packageManager.timeTable[key])
            self.unloadPackage(nextPackage[0])
            
            #print(f'unloading package ID: {nextPackage[0]}')
            #print(f'time is {self.time}')
            
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
    

    