from threading import *

def displayNumbers():
    num = 0
    trd = current_thread().getName()# invoke the current_thread method for info about current thread
    print(trd)
    while (num<=10):
        print(num)
        num+=1
trd = current_thread().getName()
print(trd)

t = Thread(target=displayNumbers)
t.start()#invoke the start method to spawn off  the threead