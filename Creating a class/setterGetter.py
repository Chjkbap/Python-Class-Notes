class Developer:
    def setName(self,name): #create the setter method
        self.name = name # assign the parameter name to the obhect variable 
    
    def getName(self): #create the getter method
        return self.name  # return the value passed into the parameter
    
    def setPay(self,salary):#create the setter method
        self.salary = salary # assign the parameter salary to the obhect variable 

    def getPay(self): #create the getter method
        return self.salary # return the value passed into the parameter

dev1 = Developer() # instance object of the class Developer
dev1.setName("Paul") # pass the value to the setter parameter using the dev1 object
dev1.setPay(4345) #pass the value to the setter parameter using the dev1 object

print (dev1.getName())
print (dev1.getPay())

# create one more instance of the class developer and use 
# setter method to set the respective values/pass in the arguments
#print the values of the object/instance of the class
