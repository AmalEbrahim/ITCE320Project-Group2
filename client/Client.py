import socket

print("\n********************The Client Has Started******************** \n")
server_address = ("192.168.1.136", 52497)

Csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Csock.connect(server_address)
my_name = input("Enter client name: ")
Csock.send(my_name.encode('ascii'))

while True:
    print("\nSelect an Option\n"
          "1. Display all arrived flights details.\n"
          "2. Display all delayed flights details.\n"
          "3. Display all flights coming from a specific city\n"
          "4. Display all details of particular flight\n"
          "5. Quit.\n")

    option = input("Sending number: ")
    Csock.send(option.encode('ascii'))
    if int(option) == 1:
        Csock.recv(1024).decode('ascii')
