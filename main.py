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
    for packageID in truck1Packages:
        address = hashTable.search(packageID).address
        truck1.loadPackage(packageID, address)
    for packageID in truck2Packages:
        address = hashTable.search(packageID).address
        truck2.loadPackage(packageID, address)
    for packageID in truck3Packages:
        address = hashTable.search(packageID).address
        truck3.loadPackage(packageID, address)

def userInterface() -> None:
    interface = menu.Menu
    interface.welcomeMessage()
    while True:
        interface.optionMenu()
        userInput = input('Please pick an option: ')
        if userInput.lower() in ['q', 'quit', 'exit', 'end', 'stop']:
            print(interface.MOTD())
            break
        if userInput.lower() in ['m', 'menu', 'help','?']:
            print('\n\n')
            interface.optionMenu()
        if userInput.lower()[0] == 's':
            try:
                # time = datetime.strptime(userInput[2:], '%H:%M').time()
                # print(str(type(time)) + str(time))
                PM.lookupTimeTable(userInput[2:]).printAll()
                continue
            except ValueError:
                print('\n**********************************************\n')
                print('Invalid time value. Please use HH:MM:SS ex: 09:30:10')
                print('\n**********************************************\n')
                continue

def buildTableOnTheFly(hashTable, queryTime):
    newHashTable = hashTable.copy()
    
    for package in newHashTable:
            
        if package.deliveryTime != 'N/A' and (time.fromisoformat(package.deliveryTime) > time.fromisoformat(queryTime)):
            package.setDeliveryTime('N/A')
            package.setDeliveryStatus('Undelivered')
    
        
    newHashTable.printAll()
    

if __name__ == "__main__":    
    truck1 = truck()
    truck2 = truck()
    truck3 = truck()
    loadPackageDataAndInsertIntoHashTable()
    #hashTable.printAll()
    loadTrucks()
    truck1.setDepartureTime(datetime.today().replace(hour=8, minute=0, second=0))
    truck2.setDepartureTime(datetime.today().replace(hour=8, minute=0, second=0))
    truck3.setDepartureTime(datetime.today().replace(hour=9, minute=25, second=41))
    dist = distance.Distance()
    dist.loadDistanceTable()
    startingTime = datetime.today().replace(hour=8, minute=0, second=0)
    PM = packageManager.packageManager()
    
    # time_str = startingTime.time().strftime("%H:%M:%S")
    # PM.addToTimeTable(time_str, hashTable.copy())
    # print(PM.timeTable)
    # startingTime = datetime.today().replace(hour=8, minute=0, second=0)
    # PM.initTimeTable(startingTime.time().strftime("%H:%M:%S"), hashTable)
    # print(PM.timeTable)

    
    #print(calculateTimeGivenDistance(7.2))

    # userInterface()
            

    
    
    
    #print(truck1)
    #print(truck2)
    #print(truck3)
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
    
    # for key in PM.timeTable:
    #     print(f'key: {key}')
    #     print(PM.timeTable[key].printAll())
    #     print("\n\n\n\n\n")
    
    
    print(f'Total distance traveled: {truck1TotalDistanceTraveled + truck2TotalDistanceTraveled + truck3TotalDistanceTraveled}')
    buildTableOnTheFly(hashTable, '09:21:09')
    # userInterface()
    
    


    
    #hashTable.printAll()
    
    #packageManager(datetime.today().replace(hour=10, minute=0, second=0, microsecond= 0), hashTable)
    
    #timeTable[datetime.today().replace(hour=10, minute=0, second=0, microsecond= 0)].printAll()
    
    #print(timeTable[datetime.today().replace(hour=10, minute=0, second=0, microsecond= 0)])
    
    # print(dist.returnAddressIndex('2835 Main St'))
    # print(dist.returnAddressIndex('HUB'))
    #print(dist.distance_table[11][1])
    #print(dist.returnDistance(11,0))
    #print(dist.returnDistance(dist.returnAddressIndex('HUB'), dist.returnAddressIndex('3365 S 900 W')))
            