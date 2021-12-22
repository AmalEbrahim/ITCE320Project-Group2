import socket
print(25*"--"+"\n The Client Has Started \n")
server_address = ("192.168.1.136", 52497)
my_name = input("Enter client name: ")

Csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Csock.connect(server_address)
Csock.send(my_name.encode('ascii'))
while True:
    print("\nEnter number:\n"
      "1. Display all arrived flights details.\n"
      "2. Display all delayed flights details.\n"
      "3. Display all flights coming from a specific city\n"
      "4. Display all details of particular flight\n"
      "5. Quit.\n")

number = input("Sending number: ")
int(number)
Csock.sendall(number.encode('ascii'))
if number == '1':
         print("All arrived flights : ")
         Directory = r'C:\Users\amool\PycharmProjects\ITCE320_Project'
         if not os.path.exists(Directory):
               os.mkdir(Directory)

         with open(Directory + '/group_ID.json', 'wb') as f:
               recvfile = Csock.recv(1048576)
               f.write(recvfile)

         with open(Directory + '/group_ID.json') as f:
               flight_Data = json.load(file)

         for flight in flightData['data']:
               print("\nFlight code (IATA) : {}\nDeparture Airport : {}, Arrival Time : {}, Terminal : {}, Gate : {}"
                     .format(flight['flight']['iata'], flight['departure']['airport'], flight['arrival']['actual'], flight['arrival']['terminal'], flight['arrival']['gate']))
elif number == '2':
         print("All delayed flights : ")
         Directory = r'C:\Users\amool\PycharmProjects\ITCE320_Project'
         if not os.path.exists(Directory):
               os.mkdir(Directory)

         with open(Directory + '/group_ID.json', 'wb') as f:
               recvfile = Csock.recv(1048576)
               f.write(recvfile)

         with open(Directory + '/group_ID.json') as f:
               flight_Data = json.load(file)
         for flight in flightData['data']:
               print("\nFlight code (IATA) : {}\nDeparture Airport : {}, Departure Time : {}, Estimated Arrival Time : {}, Terminal : {}, Gate : {}"
                     .format(flight['flight']['iata'], flight['departure']['airport'], flight['departure']['actual'],flight['arrival']['estimated'], flight['arrival']['terminal'], flight['arrival']['gate']))
elif number == '3':
elif number == '4':
elif number == '5':
        print(cs.recv(1024).decode('ascii'))  # Client receives goodbye
        print("\nClient closed\n" + 25 * "=")
        break

   else:
      print(cs.recv(1024).decode('ascii'))  # When client enters a wrong number

Csock.close()
option = input("Sending number: ")
Csock.send(option.encode('ascii'))
