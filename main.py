import csv
import random
from package import Package
import chainingHashTable
import distance
import menu
from datetime import date, datetime, timedelta
from truck import truck

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
    truck3Packages = [9,25,26,28,32,10,2,33,11,17,24]
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
                time = datetime.strptime(userInput[2:], '%H:%M').time()
                print(str(type(time)) + str(time))
                continue
            except ValueError:
                print('\n**********************************************\n')
                print('Invalid time value. Please use HH:MM ex: 09:30')
                print('\n**********************************************\n')
                continue
    
    
    return 

'''
below we are creating a dictionary where the key is the time and the value is a copy of 
the hash table at that given time. This way we can print the status of packages at that 
time by just printing the value of the dictionary

so when someone asks for the status at something like 9:30 we can just do something like print(packageManager[time]) something 
we will have to look out for though is if the time requested is not in the hash table in which case we might just want to decrement by 1
something like 

while time not in hash table:
    time = time - 1
    
this is because we want to get the previous status because we can not look into the future 
'''

timeTable = {}

def packageManager(time, hashTable):
    timeTable[time] = hashTable




if __name__ == "__main__":    
    truck1 = truck()
    truck2 = truck()
    truck3 = truck()
    

    
    #print(calculateTimeGivenDistance(7.2))

    # userInterface()
            
    loadPackageDataAndInsertIntoHashTable()
    loadTrucks()
    truck1.startDeliveryRoute()
    print(truck1)
    # print(truck2)
    # print(truck3)
       
    dist = distance.Distance()
    dist.loadDistanceTable()
    
    #hashTable.printAll()
    
    packageManager(datetime.today().replace(hour=10, minute=0, second=0, microsecond= 0), hashTable)
    
    #timeTable[datetime.today().replace(hour=10, minute=0, second=0, microsecond= 0)].printAll()
    
    #print(timeTable[datetime.today().replace(hour=10, minute=0, second=0, microsecond= 0)])
    
    # print(dist.returnAddressIndex('2835 Main St'))
    # print(dist.returnAddressIndex('HUB'))
    #print(dist.distance_table[11][1])
    #print(dist.returnDistance(11,0))
    #print(dist.returnDistance(dist.returnAddressIndex('HUB'), dist.returnAddressIndex('3365 S 900 W')))
            