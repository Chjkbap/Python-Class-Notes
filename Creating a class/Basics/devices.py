# Object Oriented programming: object have three things
#  Identity/Name, Properties/Variables, Functionality/Behaviour.
# Objects communicates with each other through Functionality and Behaviours, 
# and exchange data via properties or variables
""" The init built in Python method available for every class and takes the
 keyword self"""
""" Self points to the current object been created of this particular class """
""" Use the init method to define and assign values to fields """

class MobilePhone:
    def __init__(self): #construct an object of the clas
        self.name = "Samsung" # use self declare and assign values
        self.description = "Slim build, touch screen" # define the field name
        self.price = 945
m1 = MobilePhone() # create an object(m1) of the class MobilePhone


#use the objectnameDOT variable/field name to access an properties and/or value
print(m1.name)
print(m1.description)
print(m1.price)
 

#Exercise create a class of your choice
#Create two instances(objects) of the class
#print the values inside the class through thier objects