            num+=1
obj= Mythread() # creat an object instance of the Mythread class
t1= Thread(target=obj.displayNumbers)#create thread object using thre thread class
t1.start()

t2= Thread(target=obj.displayNumbers)#create thread object using thre thread class
t2.start()

t3= Thread(target=obj.displayNumbers)#create thread object using thre thread class
t3.start()