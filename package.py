class Package:
    def __init__ (self,
        packageID = 0,
        address = '',
        city = '',
        state = '',
        zip = 0,
        deliveryDeadLine = '',
        weight = 0,
        deliveryStatus = 0,
        deliveryTime = 'Undelivered',):
        
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadLine = deliveryDeadLine
        self.weight = weight
        self.deliveryStatus = deliveryStatus
        self.deliveryTime = deliveryTime
        
    def setPackageID(self, ID):
        self.packageID = ID
    def setAddress(self, address):
        self.address = address
    def setCity(self, city):
        self.city = city
    def setState(self, state):
        self.state = state
    def setZip(self, zip):
        self.zip = zip
    def setDeliveryDeadLine(self, deadline):
        self.deliveryDeadLine = deadline
    def setWeight(self, weight):
        self.weight = weight
    def setDeliveryStatus(self, status):
        self.deliveryStatus = status
    def setDeliveryTime(self, time):
        self.deliveryTime = time
    def getStatus(self):
        print(f'Package:{self.packageID} | Address: {self.address}')
    def returnStringRepresentation(self):
        return f"{'Package ID: ' + self.packageID:<15} | {'Address: '+ self.address:<48} | {'City: ' + self.city:<25} | {'State: ' + self.state:<10} | {'Zip: ' + self.zip:<10} | {'Delivery Deadline: ' + self.deliveryDeadLine:<28} | {'Weight: ' + str(self.weight):<10} | {'Delivery Status: ' + str(self.deliveryStatus):<25} | {'Delivery Time: ' + self.deliveryTime:<12}"
    
    # def __repr__(self):
    #     return f"{'Package ID: ' + self.packageID:<15} | {'Address: '+ self.address:<48} | {'City: ' + self.city:<25} | {'State: ' + self.state:<10} | {'Zip: ' + self.zip:<10} | {'Delivery Deadline: ' + self.deliveryDeadLine:<28} | {'Weight: ' + str(self.weight):<10} | {'Delivery Status: ' + str(self.deliveryStatus):<25} | {'Delivery Time: ' + self.deliveryTime:<12}"