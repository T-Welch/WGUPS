import distance
from datetime import datetime, timedelta
class truck:
    
    
    def __init__(self):
        self.truckNumber = 0
        self.truckDepartureTime = datetime.today().replace(hour=0, minute=0, second=0).time
        self.time = self.truckDepartureTime
        self.packages = []
        self.currentLocation = 'HUB'
        self.distanceTraveled = 0
        
        self.distanceObj = distance.Distance()
        self.distanceObj.loadDistanceTable()
        
    def setTime(self, time):
        self.time = time
    def setDepartureTime(self,time):
        self.time = time
        self.truckDepartureTime = time
  
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
    
    #this is the logic behind the delivering of packages. When main calls this function all of the magic happens
    
    def startDeliveryRoute(self, packageManager, packageHashTable) -> tuple:       
        #while the truck still has packages     
        while self.isNotEmpty():
            #the variables get overwritten making the names apt at times and confusing at others but if you follow the flow they make sense
            #this basically takes two values (current location and the list of packages remaining) and calculates which package is 
            #closest to the current location then returns a tuple with the package to deliver and the distance
            nextPackage, nextPackageDistance = self.distanceObj.nearestNeighbor(self.currentLocation, self.packages)
                
            #now we need to calculate how long it will take to travel that distance 
            self.addTime(self.distanceObj.calculateTimeGivenDistance(nextPackageDistance))
            #and add that distance to the total distance traveled
            self.addDistance(nextPackageDistance)
            #update the current location to the address of the package that we just drove to deliver
            self.currentLocation = nextPackage[1]
            #update the status of that package 
            #the original idea was to create a hashTable of times of deliveries and statuses at that time but I scrapped that in favor of the 
            #build the table on the fly function in the main program so it is commented out. It was an okay idea but the building the table on the fly is better in my opinion 
            packageHashTable[nextPackage[0]].setDeliveryStatus('Delivered')
            packageHashTable[nextPackage[0]].setDeliveryTime(self.time.strftime("%H:%M:%S"))
            # time_str = self.time.strftime("%H:%M:%S")
            # packageManager.addToTimeTable(time_str, packageHashTable.copy())
            # key = self.time.strftime("%H:%M:%S")
            # packageManager.addToTimeTable(key, packageHashTable)
            self.unloadPackage(nextPackage[0]) 
                        
        # when the truck is empty it needs to return to the hub because that's where the trucks live and the driver can't just take it home 
        distanceToHUB = self.distanceObj.returnDistance(self.distanceObj.returnAddressIndex(self.currentLocation),self.distanceObj.returnAddressIndex('HUB'))
        self.addDistance(distanceToHUB)
        self.addTime(self.distanceObj.calculateTimeGivenDistance(distanceToHUB))
        #calculate how long the truck operated for
        time_difference = self.time - self.truckDepartureTime
        timeString = str(time_difference).split(':')
        formattedTimeDifference = "{}:{}:{}".format(timeString[0].zfill(2), timeString[1], timeString[2][:2])
        return self.truckDepartureTime, formattedTimeDifference, self.distanceTraveled

            

        # return self.truckDepartureTime, timedelta(self.time - self.truckDepartureTime), self.distanceTraveled
            
        #he below functions are just basic setters for variables that are used inside of the object
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
    
    #__repr__ was a cool bit of python wizardry that I learned about while doing this project and I now love it. 
    #this just allows for easier debugging when modifying the project
    
    def __repr__(self) -> str:
        return f'Packages in this truck: {self.packages} distance traveled: {self.distanceTraveled}'
    

    