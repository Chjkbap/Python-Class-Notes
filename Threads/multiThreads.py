from threading import * # import thread which is a class in the threading module
from time import sleep

class Mythread: # define that extends Thread(superclass)
    def displayNumbers(self): #
        print(current_thread().getName())
        sleep(1)
        num = 0
        while (num<=10):
            print(num)
            num+=1
obj= Mythread() # creat an object instance of the Mythread class
t1= Thread(target=obj.displayNumbers)#create thread object using thre thread class
t1.start()

t2= Thread(target=obj.displayNumbers)#create thread object using thre thread class
t2.start()

t3= Thread(target=obj.displayNumbers)#create thread object using thre thread class
t3.start()