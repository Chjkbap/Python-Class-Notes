import socket #import socket module 

host = 'localhost' # define host = local host

port = 6767  # assign port number to port

''' invoke the socket module class to create a socket and use the socket constant "AF_INET" to specify version of IP to use 
and pass it as a parameter. The second parameter "socket.SOCK_STREAM"  is used to pass in the type of connection, which is TCP IP '''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

''' used the bind method to bind socket to host port and pass host and port parameter within the braces of the bind method'''
s.bind((host,port))

'''  invoke s.listen method to start up the server and pass in the number of connections server will accept as parameter  '''
print("Server listening on port:", port)
s.listen(1)

''' invoke s.accept method to accept client connect request when a client tries to connect to the server. This methods returns 
the connection object and the address from which the request came from '''


c, addr = s.accept()

fileName = c.recv(1024) #invoke s.recv to received the file and assigned it to file object, fileName  variable

try:
    f = open(fileName, "rb") #use file open object and pass the file name and pass the rb parameter to read binary
    content = f.read() # read the contents of the file
    c.send(content) # send the contents of the file back to the client
    f.close()
except FileNotFoundError:
    print("File not found ")
    c.send(b"File does not exist ") #send binary encoded message back to client File not found "

c.close()#closes connection