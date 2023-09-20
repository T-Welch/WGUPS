import csv
class Distance:
    def __init__(self):
        
        self.distance_table = []
    
    
    def loadDistanceTable(self):
        with open('distance_table.csv', newline = '') as DTCSV:
            DT = csv.reader(DTCSV, delimiter=',')
            for line in DT:
                row = line[0]
                row_data = [float(value) if value else None for value in line[1:]]
                self.distance_table.append([row] + row_data)
                    
        # for entry in self.distance_table:
        #     print(entry)
                
                
            
    
    def returnAddressIndex(self, address) -> int:
        for i, line in enumerate(self.distance_table):
            if line[0] == address:
                return i
        return -1
    
    def returnDistance(self, index1, index2) -> float:
        
        bigger, smaller = (index1, index2) if index1 > index2 else (index2, index1)
        
        return self.distance_table[bigger][smaller + 1]
    def calculateTimeGivenDistance(distance) -> float:
    
        fractional_time = distance/18
        return(60 * fractional_time)