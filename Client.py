import socket
print(25*"--"+"\n The Client Has Started \n")
Csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Csock.connect(("192.168.1.104", 52497))
