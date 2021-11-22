''' abstract class can't be instatiated. One method has to be an abstract class'''

from abc import abstractmethod, ABC

class Car(ABC): # parent class inherits from the ABC to mandate all child classes implemnet the abstract method
    def __init__(self, make, model, year): # paren class constructor and parameters
        self.make = make
        self.model = model
        self.year = year

    def startCar(self):
        print("Starting the car...")
    
    @abstractmethod  # mark with the abstrac decorator  
    def driveCar(self):
        pass

    def stopCar(self):
        print("Stopping the car...")
    # add and invoke a method of your choice

class Bmw(Car): #child class
    def __init__(self,cruisedControlled, make, model, year):# inheritted parent class fields through child class constructor
        super().__init__(make, model, year) # invoke parent class constructor using the super method and passing its parameters
        self.cruisedControlled = cruisedControlled
    
    def displayBmw(self):
        print("The colour of my BMW is white")

    def startCar(self): # ovrriding/shadow functionality from the parent class
        print("Remote Start")
        super().startCar() # invoking the parent class method within the child class

    def driveCar(self):
        print("drive car")
          
class Merc(Car):
    def __init__(self, parkingAssist, make, model, year):
        Car.__init__(self, make, model, year)
        self.parkingAssist = parkingAssist
   #overide the startCar method here 
   #Print....key start/button start
   
   #use the super method
   # call the start method using the super method/function
   
    def driveCar(self):
        print("drive car")

        
bmwCar = Bmw (True, "BMW", "312E", 2017)
mercCar = Merc (True, "Benz", "190", 1999)

print(bmwCar.make)
print(bmwCar.model)
print(bmwCar.year)
print(bmwCar.cruisedControlled)

bmwCar.displayBmw()

bmwCar.startCar()
print(f"I am driving a {bmwCar.year} {bmwCar.make}")
bmwCar.stopCar()
bmwCar.driveCar()

print(mercCar.make)
print(mercCar.model)
print(mercCar.year)
print(mercCar.parkingAssist)

mercCar.startCar()
print(f"I am driving a {mercCar.year} {mercCar.make}")
mercCar.stopCar()
#create  one more child class
# create an instance of the child class
# print out the properties and values of the object instance
        