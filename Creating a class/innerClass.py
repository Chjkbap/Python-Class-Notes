class Car:
    def __init__(self,make, year):
        self.make = make
        self.year = year
    
    class CarEngine:
        def __init__(self, engineNum):
            self.engineNum = engineNum

        def startCar(self):
            print("Engine started....")

c1 = Car('Benz', 2018)
carEng1 = c1.CarEngine(1234)


print(c1.make)
print(c1.year)
print(carEng1.engineNum)
carEng1.startCar()

#create two more instances/object of the class Car
# Pass in different values and display the result
