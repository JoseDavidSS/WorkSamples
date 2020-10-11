class Car:
    def __init__(self, color, plate, model, topVelocity, weight, price):
        
        self.color = color
        self.plate = plate
        self.model = model
        self.topVelocity = topVelocity
        self.weight = weight
        self.price = price
        self.owners = []
        
# Gets y Sets..............................................................

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
        
    def getPlate(self):
        return  self.plate
    def setPlate(self, plate):
        self.plate = plate

    def getModel(self):
        return  self.model
    def setModel(self, model):
        self.model = model

    def getTopVelocity(self):
        return  self.topVelocity
    def setTopVelocity(self, topVelocity):
        self.topVelocity = topVelocity

    def getWeight(self):
        return  self.weight
    def setWeight(self, weight):
        self.weight = weight

    def getPrice(self):
        return  self.price
    def setPrice(self,price):
        self.price = price

    def getOwners(self):
        return  self.owners
    def setOwners(self,owners):
        self.owners = owners
        
#........................................................................

    def addOwners(self, newOwner):
        self.owners.append(newOwner)

    def searchOwner(self, newOwner):
        length = len(self.owners)
        return self.searchOwnerAux(newOwner, length, 0)
    
    def searchOwnerAux(self, newOwner, length, counter):
        if counter == length:
            return False
        elif self.owners[counter] == newOwner:
            return True
        else:
            return self.searchOwnerAux(newOwner, length, counter+1)
    
    def printCarData(self):
        print("Car's color is: ", self.color)
        print("Car's plate is: ", self.plate)
        print("Car's model is: ", self.model)
        print("Car's price: ", self.price)
        
    def riseTax(self):
        if (self.price > 4000000):
            self.price = self.price * (1.05)
        else:
            self.price = self.price * (1.02)
            
        
# Object example ends here

myCar = Car("black", "VVV-56", "Corolla", 50, 1000, 100000)
myCar.addOwners("Jose")
myCar.addOwners("Jorge")
myCar.addOwners("Maria")
myCar.printCarData()





