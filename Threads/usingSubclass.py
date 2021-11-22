from threading import Thread # import thread which is a class in the threading module

class Mythread(Thread): # define that extends Thread(superclass)
    def run(self): #
        num = 0
        while (num<=10):
            print(num)
            num+=1
t= Mythread() # creat an object instance of the Mythread class
t.start()
