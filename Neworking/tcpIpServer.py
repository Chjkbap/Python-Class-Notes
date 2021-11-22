import socket 

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

print("listening on port:",port)

s.listen(2)
c, addr = s.accept()

print("connection from", str(addr))

c.send(b"Hello how are you...doing")
c.send("Thank and good bye".encode())
c.close()