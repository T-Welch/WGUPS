import csv
from package import Package
import chainingHashTable
import distance

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
                print(hashTable.search(newPackage.packageID))
                #except AttributeError:
                #    print('non issue')
        
        
            
    loadPackageDataAndInsertIntoHashTable()
    
       
    dist = distance.Distance
    dist.loadDistanceTable(dist)
            