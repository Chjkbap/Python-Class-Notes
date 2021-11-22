# Inheritance is the process of defining a new object with the help of an existing object
#  Two inheritance key principles are as follows
#  1. Accessing existing objects functionality 
#  2. Updating existing objects functionality
#  Two other key terms are as follows
#  1. Re-Usability and 2. IS-A Relation

class Car: # parent class
    def __init__(self, make, model, year): # paren class constructor and parameters
        self.make = make
        self.model = model
        self.year = year

class Bmw(Car): #child class
    def __init__(self,cruisedControlled, make, model, year):# inheritted parent class fields through child class constructor
        Car.__init__(self, make, model, year) # invoke parent class constructor passing its parameters
        self.cruisedControlled = cruisedControlled

class Merc(Car):
    def __init__(self, parkingAssist, make, model, year):
        Car.__init__(self, make, model, year)
        self.parkingAssist = parkingAssist
        
bmwCar = Bmw (True, "BMW", "312E", 2017)
mercCar = Merc (True, "Benz", "190", 1999)

print(bmwCar.make)
print(bmwCar.model)
print(bmwCar.year)
print(bmwCar.cruisedControlled)

print(f"I am driving a {bmwCar.year} {bmwCar.make}")


print(mercCar.make)
print(mercCar.model)
print(mercCar.year)
print(mercCar.parkingAssist)

print(f"I am driving a {mercCar.year} {mercCar.make}")

#create  one more child class
# create an instance of the child class
# print out the properties and values of the object instance
        