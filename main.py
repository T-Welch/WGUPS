import csv
import random
from package import Package
import chainingHashTable
import distance
import menu
from datetime import date, datetime, timedelta

if __name__ == "__main__":    
    
    def loadPackageDataAndInsertIntoHashTable():
        with open('packages.csv', newline='') as csvfile:
            # PD will be shorthand for package data for ease of use
            PD = csv.reader(csvfile, delimiter= ',')
            # packageList = []
            hashTable = chainingHashTable.chainingHashTable()
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
                # packageList.append(newPackage)
                #try:
                #print(type(newPackage.packageID))
                #print(hashTable.search(newPackage.packageID))
                #except AttributeError:
                #    print('non issue')
        
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
    
    userInterface()
            
    loadPackageDataAndInsertIntoHashTable()
    
       
    dist = distance.Distance()
    dist.loadDistanceTable()
    # print(dist.returnAddressIndex('2835 Main St'))
    # print(dist.returnAddressIndex('HUB'))
    #print(dist.distance_table[11][1])
    #print(dist.returnDistance(11,0))
    #print(dist.returnDistance(dist.returnAddressIndex('HUB'), dist.returnAddressIndex('3365 S 900 W')))
            