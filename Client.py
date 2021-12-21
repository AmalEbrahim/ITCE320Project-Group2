import socket
print(25*"--"+"\n The Client Has Started \n")
server_address = ("192.168.1.104", 52497)
my_name = input("Enter client name: ")

Csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Csock.connect(server_address)
Csock.send(my_name.encode('ascii'))

print("\nEnter number:\n"
      "1. All arrived flights.\n"
      "2. Delayed flights.\n"
      "3. All flights coming from a specific city\n"
      "4. Details of particular flight\n"
      "5. Quit.\n")

number = input("Sending number: ")
int(number)
