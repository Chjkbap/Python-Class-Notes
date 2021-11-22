# Encapsulation is protecting the properties and the functionalities of an object
#from other objects

class Learner:
    def setId(self, sId): # create a setter metthod along with the parameter
        self.sId = sId

    def getId(self): # define a getter method which does require additional parameters
        return self.sId
    
    # add a setter and a getter method for name
    # access it using the setter method

l1 = Learner()
l1.setId(1001) # pass the arguments/values to the setter parameter

#print(l1.sId)
print(l1.getId())



    
