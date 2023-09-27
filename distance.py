import csv
class Distance:
    def __init__(self):
        
        self.distance_table = []
    
    #this is how we load the distane csv, this then populates a list (array) of lists (arrays)
    #from this list we can calculate distances between destinations
    def loadDistanceTable(self):
        with open('distance_table.csv', newline = '') as DTCSV:
            DT = csv.reader(DTCSV, delimiter=',')
            for line in DT:
                row = line[0]
                row_data = [float(value) if value else None for value in line[1:]]
                self.distance_table.append([row] + row_data)
                
            
    #this is a function to take in a string (address)
    #and return which index location that address is at in the array 
    #allowing for better readability in other functions
    def returnAddressIndex(self, address) -> int:
       addressList = ["HUB",
        "1060 Dalton Ave S",
        "1330 2100 S",
        "1488 4800 S",
        "177 W Price Ave",
        "195 W Oakland Ave",
        "2010 W 500 S",
        "2300 Parkway Blvd",
        "233 Canyon Rd",
        "2530 S 500 E",
        "2600 Taylorsville Blvd",
        "2835 Main St",
        "300 State St",
        "3060 Lester St",
        "3148 S 1100 W",
        "3365 S 900 W",
        "3575 W Valley Central Station bus Loop",
        "3595 Main St",
        "380 W 2880 S",
        "410 S State St",
        "4300 S 1300 E",
        "4580 S 2300 E",
        "5025 State St",
        "5100 South 2700 West",
        "5383 S 900 East #104",
        "600 E 900 South",
        "6351 South 900 East"]
       
       return addressList.index(address)
            
        #this takes in two locations and returns the distance. we need to figure out which is bigger because that will
        #dictate which one we use as the first index because it will have more complete information on the distance table
    def returnDistance(self, index1, index2) -> float:
        
        bigger, smaller = (index1, index2) if index1 > index2 else (index2, index1)
        
        return self.distance_table[bigger][smaller + 1]
    #this returns the time it takes to travel a certain distance since our speed is a constant 
    def calculateTimeGivenDistance(self,distance) -> float:
    
        fractional_time = distance/18
        return(60 * fractional_time)
    
    #this is the nearest neighbor algo. it is a greedy algo which takes a current location and a list of locations
    #it then checks which address is closest and returns that package and the distance to that address
    
    def nearestNeighbor(self, currentLocation, listOfPackages) -> tuple:
        nextPackage = None
        nextPackageDistance = float("inf")
        for package in listOfPackages:
            if self.returnDistance(self.returnAddressIndex(currentLocation),self.returnAddressIndex(package[1]) ) < nextPackageDistance:
                nextPackage = package
                nextPackageDistance = self.returnDistance(self.returnAddressIndex(currentLocation),self.returnAddressIndex(package[1]) )
        return(nextPackage, nextPackageDistance)