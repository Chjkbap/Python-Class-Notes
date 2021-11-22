# Encapsulation is protecting the properties and the functionalities of an object
#from other objects

class Learner:
    def __init__(self):
        self.__id = 123 # use double underscore to create a private field which can't be access outside it's class
        self.__name ="Paul" #use double underscore to create a private field which can't be access outside it's class
    # add three more private fields 
    # access the field using one or both methods(via method/function and/or name mangling)

    #another way to access private fields is through function/method
    def displayFields(self):
        print(self.__id)
        print(self.__name)

l1 = Learner()

l1.displayFields()
# print(l1.id)
# print(l1.name)

#one way to access private fields is through name mangling
print(l1._Learner__id) # name mangling is used to access private fields because they are not completely hidden
print(l1._Learner__name) # name mangling is used to access private fields because they are not completely hidden
        