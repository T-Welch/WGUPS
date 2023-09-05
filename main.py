import csv
from package import Package

if __name__ == "__main__":
    with open('packages.csv', newline='') as csvfile:
        # PD will be shorthand for package data for ease of use
        PD = csv.reader(csvfile, delimiter= ',')
        next(PD)
        packageList = []
        for box in PD:
            newPackage = Package()
            newPackage.setPackageID(box[0])
            newPackage.setAddress(box[1])
            newPackage.setCity(box[2])
            newPackage.setState(box[3])
            newPackage.setZip(box[4])
            newPackage.setDeliveryDeadLine(box[5])
            newPackage.setWeight(box[6])
            packageList.append(newPackage)
            
            # print(' '.join(package))
        for package in packageList:
            print(package)
            
            
            
            
    
    