# Polymorphism, poly means multi and morphic means shapes.in OOP shapes means behaviour
# Different benhaviour based on the data or objects that the functions are dealing with.
# Polymorphism in python through duck typing
class Cat:
    def talking(self): # method talking
        print("Meeoow")

class Person:
    def talking(self):
        print("Hello....you")

# add a class with talking method
# create an instance object of the class
# use callTalking function to display behaviour of the class

# create a function/method callTalinkg without spefifying the type of object and obj as the
#  parameter toinvoke any method on the object
def callTalking(obj):
    obj.talking()
 
c = Cat() # create an object instance 
callTalking(c)

p = Person()
callTalking(p)


