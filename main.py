import csv
import random
from package import Package
import chainingHashTable
import distance
import menu
from datetime import date, datetime, timedelta
from truck import truck

hashTable = chainingHashTable.chainingHashTable()

def loadPackageDataAndInsertIntoHashTable():
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
                      
def loadTrucks():
    truck1Packages = [30,8,27,35,40,4,37,5,29,7,39,31,1]
    truck2Packages = [6,3,14,15,34,13,16,18,19,20,21,36,38,22,12,23]
    truck3Packages = [9,25,26,28,32,10,2,33,11,17,24]
    for package in truck1Packages:
        truck1.loadPackage(package)
    for package in truck2Packages:
        truck2.loadPackage(package)
    for package in truck3Packages:
        truck3.loadPackage(package)
def userInterface():
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

packageManagmentTable = {}
def packageManager():
    return
    

def calculateTimeGivenDistance(distance):
    
    fractional_time = distance/18
    return(fractional_time , 60 * fractional_time)
    




if __name__ == "__main__":    
    truck1 = truck()
    truck2 = truck()
    truck3 = truck()
    
    print(calculateTimeGivenDistance(7.2))

    # userInterface()
            
    loadPackageDataAndInsertIntoHashTable()
    loadTrucks()
    print(truck1)
    print(truck2)
    print(truck3)
       
    dist = distance.Distance()
    dist.loadDistanceTable()
    
    hashTable.print_all()
    
    # print(dist.returnAddressIndex('2835 Main St'))
    # print(dist.returnAddressIndex('HUB'))
    #print(dist.distance_table[11][1])
    #print(dist.returnDistance(11,0))
    #print(dist.returnDistance(dist.returnAddressIndex('HUB'), dist.returnAddressIndex('3365 S 900 W')))
            