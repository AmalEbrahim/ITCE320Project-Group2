import socket
print(25*"--"+"\n The Client Has Started \n")
server_address = ("192.168.1.136", 52497)
my_name = input("Enter client name: ")

Csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Csock.connect(server_address)
Csock.send(my_name.encode('ascii'))

print("\nEnter number:\n"
      "1. Display all arrived flights details.\n"
      "2. Display all delayed flights details.\n"
      "3. Display all flights coming from a specific city\n"
      "4. Display all details of particular flight\n"
      "5. Quit.\n")

option = input("Sending number: ")
Csock.send(option.encode('ascii'))
