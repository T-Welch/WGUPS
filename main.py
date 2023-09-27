# Trevor Welch Student ID:010892085 
import csv
import random
from package import Package
import chainingHashTable
import distance
import menu
from datetime import date, datetime, timedelta, time
from truck import truck
import packageManager

# first thing we have to do it create a new hashTable object from my custom hash table class

hashTable = chainingHashTable.chainingHashTable()

#this is a function that takes the package data from the csv file and we create a new package object and store the data into the newly created hash table using the package ID as the key 

def loadPackageDataAndInsertIntoHashTable() -> None:
        with open('packages.csv', newline='') as csvfile:
            PD = csv.reader(csvfile, delimiter= ',')
            # packageList = []
            
            for box in PD:
                
                newPackage = Package()
                newPackage.setPackageID(int(box[0]))
                newPackage.setAddress(box[1])
                newPackage.setCity(box[2])
                newPackage.setState(box[3])
                newPackage.setZip(box[4])
                newPackage.setDeliveryDeadLine(box[5])
                newPackage.setWeight(box[6])
                newPackage.setDeliveryTime('N/A')
                newPackage.setDeliveryStatus('at hub')
                hashTable.insert(newPackage.packageID, newPackage)   
                    
# this function will be used after the truck objects are created and it's purpose is to take the lists of packages 
# that are for each truck and load all of those packages on the truck
# the departure time is also manually set as we do have some packages that will delay departure of the trucks.
# we also use this function to set the "en route" time of the packages. This is the time that the packages change state
# from "at the hub" to "en route"                  

def loadTrucks() -> None:
    truck1Packages = [35,40,4,37,5,29,7,31,1,13,15,14,19,16,20,34]
    truck2Packages = [6,3,18,21,36,38,22,12,23,30,27]
    truck3Packages = [9,25,28,26,32,10,2,33,11,17,24,8,39]
    truck1.setDepartureTime(datetime.today().replace(hour=8, minute=0, second=0))
    truck2.setDepartureTime(datetime.today().replace(hour=9, minute=5, second=1))
    truck3.setDepartureTime(datetime.today().replace(hour=9, minute=45, second=41))
    for packageID in truck1Packages:
        address = hashTable.search(packageID).address
        truck1.loadPackage(packageID, address)
        hashTable[packageID].setEnRouteTime(truck1.truckDepartureTime.time())
        
    for packageID in truck2Packages:
        address = hashTable.search(packageID).address
        truck2.loadPackage(packageID, address)
        hashTable[packageID].setEnRouteTime(truck2.truckDepartureTime.time())
    for packageID in truck3Packages:
        address = hashTable.search(packageID).address
        truck3.loadPackage(packageID, address)
        hashTable[packageID].setEnRouteTime(truck3.truckDepartureTime.time())
        
#this function creates the userInterface for the program
# it takes user input and displays certain information based on that input. if incorrect input is entered it reprompts.

def userInterface() -> None:
    interface = menu.Menu
    interface.welcomeMessage()
    while True:
        interface.optionMenu()
        userInput = input('Please pick an option: ')
        if userInput.lower() in ['q', 'quit', 'exit', 'end', 'stop']:
            break
        if userInput.lower() in ['m', 'menu', 'help','?']:
            print('\n\n')
            interface.optionMenu()
        if userInput.lower()[0] == 's':
            try:

                buildTableOnTheFly(hashTable, userInput[2:])
                print(f'\n\nTotal distance traveled: {truck1TotalDistanceTraveled + truck2TotalDistanceTraveled + truck3TotalDistanceTraveled}')

                
                exit()
            except ValueError:
                print('\n**********************************************\n')
                print('Invalid time value. Please use HH:MM:SS ex: 09:30:10')
                print('\n**********************************************\n')
                continue
        if userInput.lower()[0] == 'p':
            ID = int(userInput[2:])
            try:
                if hashTable.search(ID):
                    
                    print(hashTable.search(ID))
                    exit()
                else: 
                    print('not a valid packageID package IDs are 1-40')
            except KeyError:
                print('not a valid packageID')
                print(userInput[2:])
        if userInput.lower()[0] == 'd':
            for i in range(1,41):
                print(hashTable[i].returnStringRepresentation())
                
#This is a function that we use to create the table that is displayed when the user requests the table for a certain time.
#because we do not have a predefined list of times that the user may want to query the table for 
#we need to accept any time and modify the information to be correct for that time
# so we make a copy of the hash table that has final information and modify values 
# to be what they would have been at that specific time

def buildTableOnTheFly(hashTable, queryTime):
    newHashTable = hashTable.copy()
    QueryTime = datetime.strptime(queryTime, '%H:%M:%S').time()
    
    for package in newHashTable:

        if (package.enRouteTime < QueryTime) and (datetime.strptime(package.deliveryTime, '%H:%M:%S').time() > QueryTime):
            
            
            package.setDeliveryStatus('en route')
        if (package.enRouteTime > QueryTime):
            package.setDeliveryStatus('at Hub')
    newHashTable.printAll()

#this is our main function. Because of the functions we are able to trim down our main function to be easier to understand. 

if __name__ == "__main__":    
    
    #first we create the trucks. trucks are created from the truck class
    
    truck1 = truck()
    truck2 = truck()
    truck3 = truck()
    
    #we load all of the package data into our custom hash table implementation 
    
    loadPackageDataAndInsertIntoHashTable()
    
    #we then load the trucks with the packages they're going to be delivering
    
    loadTrucks()
    
    #from there we need to create a distance class instance in order to load the provided distance table. 
    # more information about the inner workings can be found in distance.py

    dist = distance.Distance()
    dist.loadDistanceTable()
    
    #we set the starting time. This is the time the trucks can leave as per the assignment requirements
    
    startingTime = datetime.today().replace(hour=8, minute=0, second=0)
    
    #we create an instance of the package manager to give to the trucks in order to do some manipulation of the packages
    
    PM = packageManager.packageManager()

    #here we start the trucks on their way. This is when the trucks start and after they're done they return some vital information
    #we return this information as a tuple from the truck class in order to assign it to variables in the main program 
    
    truck1DeparturefromHUBTime, truck1TotalTimeTaken, truck1TotalDistanceTraveled = truck1.startDeliveryRoute(PM, hashTable)
    truck2DeparturefromHUBTime, truck2TotalTimeTaken, truck2TotalDistanceTraveled = truck2.startDeliveryRoute(PM, hashTable)
    truck3DeparturefromHUBTime, truck3TotalTimeTaken, truck3TotalDistanceTraveled = truck3.startDeliveryRoute(PM, hashTable)

    #from there we just need to add up all of the distances the trucks traveled and show it to the user
    print(f'Total distance traveled: {truck1TotalDistanceTraveled + truck2TotalDistanceTraveled + truck3TotalDistanceTraveled}')
    #here we call the user interface. All of the work is done, now we just need to show it to the user. 
    #the user will interact with the user interface in order to display the information that they request 
    userInterface()
    
    
        
  