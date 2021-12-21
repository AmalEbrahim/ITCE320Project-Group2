import socket
print(25*"--"+"\n The Client Has Started \n")
server_address = ("192.168.1.104", 52497)
my_name = input("Enter client name: ")
Csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Csock.connect(server_address)
Csock.send(my_name.encode('ascii'))
