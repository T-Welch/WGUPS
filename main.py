import csv
import random
from package import Package
import chainingHashTable
import distance
import menu
from datetime import date, datetime, timedelta, time
from truck import truck
import packageManager

hashTable = chainingHashTable.chainingHashTable()

def loadPackageDataAndInsertIntoHashTable() -> None:
        with open('packages.csv', newline='') as csvfile:
            # PD will be shorthand for package data for ease of use
            PD = csv.reader(csvfile, delimiter= ',')
            # packageList = []
            
            for box in PD:
                
                #print(type(box[0]))
                newPackage = Package()
                newPackage.setPackageID(int(box[0]))
                newPackage.setAddress(box[1])
                newPackage.setCity(box[2])
                newPackage.setState(box[3])
                newPackage.setZip(box[4])
                newPackage.setDeliveryDeadLine(box[5])
                newPackage.setWeight(box[6])
                hashTable.insert(newPackage.packageID, newPackage)   
                    
                      
def loadTrucks() -> None:
    truck1Packages = [30,8,27,35,40,4,37,5,29,7,39,31,1]
    truck2Packages = [6,3,14,15,34,13,16,18,19,20,21,36,38,22,12,23]
    truck3Packages = [9,25,28,26,32,10,2,33,11,17,24]
    truck1.setDepartureTime(datetime.today().replace(hour=8, minute=0, second=0))
    truck2.setDepartureTime(datetime.today().replace(hour=8, minute=0, second=0))
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

def buildTableOnTheFly(hashTable, queryTime):
    newHashTable = hashTable.copy()
    QueryTime = datetime.strptime(queryTime, '%H:%M:%S').time()
    
    for package in newHashTable:

        if (package.enRouteTime < QueryTime) and (datetime.strptime(package.deliveryTime, '%H:%M:%S').time() > QueryTime):
            
            
            package.setDeliveryStatus('en route')
        if (package.enRouteTime > QueryTime):
            package.setDeliveryStatus('at Hub')
    newHashTable.printAll()

if __name__ == "__main__":    
    truck1 = truck()
    truck2 = truck()
    truck3 = truck()
    loadPackageDataAndInsertIntoHashTable()
    loadTrucks()
    

    dist = distance.Distance()
    dist.loadDistanceTable()
    startingTime = datetime.today().replace(hour=8, minute=0, second=0)
    PM = packageManager.packageManager()


    truck1DeparturefromHUBTime, truck1TotalTimeTaken, truck1TotalDistanceTraveled = truck1.startDeliveryRoute(PM, hashTable)
    print(f"\n\n\n\n Truck1 finished!!!!!\
        Truck1 stats:\
        Time taken: {truck1TotalTimeTaken} \
        Distance Traveled: {truck1TotalDistanceTraveled}\
          \n\n\n\n\n")
    truck2DeparturefromHUBTime, truck2TotalTimeTaken, truck2TotalDistanceTraveled = truck2.startDeliveryRoute(PM, hashTable)
    print(f"\n\n\n\n Truck2 finished!!!!!\
        Truck1 stats:\
        Time taken: {truck2TotalTimeTaken} \
        Distance Traveled: {truck2TotalDistanceTraveled}\
          \n\n\n\n\n")
    truck3DeparturefromHUBTime, truck3TotalTimeTaken, truck3TotalDistanceTraveled = truck3.startDeliveryRoute(PM, hashTable)
    print(f"\n\n\n\n Truck3 finished!!!!!\
        Truck3 stats:\
        Time taken: {truck3TotalTimeTaken} \
        Distance Traveled: {truck3TotalDistanceTraveled}\
          \n\n\n\n\n")
    
    userInterface()
    
    
    print(f'Total distance traveled: {truck1TotalDistanceTraveled + truck2TotalDistanceTraveled + truck3TotalDistanceTraveled}')    
  