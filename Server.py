import socket
import threading

print(25 * "--" + "\n The Server Has Started \n")
Ssock_p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Ssock_p.bind(("192.168.1.104", 52497))
Ssock_p.listen(3)


def accept_connection(sock):
    data = sock.recv(1024).decode('ascii')


while True:
    Ssock_a, sockName = Ssock_p.accept()
    t = threading.Thread(target=accept_connection, args=Ssock_a)
    t.start()
