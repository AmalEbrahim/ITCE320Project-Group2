import socket
print(25*"--"+"\n The Client Has Started \n")
Csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Csock.connect(("192.168.1.104", 52497))

print("\nEnter number:\n"
      "1. Receive a list of the currently connecting clients.\n"
      "2. All arrived flights.\n"
      "3. Delayed flights.\n"
      "4. All flights coming from a specific city\n"
      "5. Details of particular flight\n"
      "6. Quit.\n")

number = input("Sending number: ")
int(number)
Csock.sendall(number.encode('ascii'))
