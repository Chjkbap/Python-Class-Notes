import socket #import socket module 


''' create an object of the socket module class '''

s = socket.socket()

s.connect(("localhost", 6767))#invoke  s.connect method to connect to the host and pass in the IP Address and port numbers parameters

fileName = input("Enter a filename: ") # request file name from user and assign it to fileName variable

s.send(fileName.encode()) #invoke the s.send method and pass in the variable file name and .encode to encode the file name

content = s.recv(1024) #invoke s.recv and pass the buffer size and assigned to content variable

print(content.decode())# #decode the encoded content received 

s.close()