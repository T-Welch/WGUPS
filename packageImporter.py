import csv
import package
class packageImporter:
    
    with open('packages.csv', newline='') as csvfile:
        packageReader = csv.reader(csvfile, delimiter= ',', quotechar= "|")
        for row in packageReader:
            print(' '.join(row))
            