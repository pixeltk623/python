# import socket
# s = socket.socket()
# print('socket Created')

# s.bind(('localhost',9999))
# s.listen(3)

# print('waiting for connection')

# while True:
# 	c, addr = s.accept()
# 	name = c.recv(1024).decode()
# 	print("Connected with ", addr, name)
# 	c.send(bytes("Welcome to Kumar", 'utf-8'))
# 	c.close()

# a = b = c = d = ''

# a, b = "5", "8"
# a = 5
# b = 7

# print(a)

# 192.168.1.4

# print(b)

import socket


s = socket.socket()

s.bind(("192.168.206.194", 9900))
s.listen(3)
print("Waiting")

f = open("client.py")

while True:
	c, addr = s.accept()
	email = c.recv(1024).decode()
	print("Connected with ", addr, email, f)
	c.send(bytes("Welcome to "+email, 'utf-8'))
	c.close()


	