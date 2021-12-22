import json
import os
import socket
import time

print("\n********************The Client Has Started******************** \n")
server_address = ("192.168.43.159", 52499)

Csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Csock.connect(server_address)
my_name = input("Enter client name: ")
Csock.send(my_name.encode('ascii'))

while True:
    print("\nSelect an Option:\n"
      "1. Display all arrived flights details.\n"
      "2. Display all delayed flights details.\n"
      "3. Display all flights coming from a specific city\n"
      "4. Display all details of particular flight\n"
      "5. Quit.\n")

    number = input("Sending number: ")
    Csock.sendall(number.encode('ascii'))
    if int(number) == 1:
        print("All arrived flights : ")
        Directory = r'C:\Users\amool\PycharmProjects\ITCE320_Project\client\client_{}'.format(my_name)
        if not os.path.exists(Directory):
            os.mkdir(Directory)
        file_path = Directory + '/G2.json'

        with open(file_path, 'wb') as file:
            recvfile = Csock.recv(1035)
            file.write(recvfile)
            time.sleep(5)

        with open(file_path) as file:
            flight_Data = json.load(file)  # Convert the JSON data into python objects

        for flight in flight_Data['data']:
            print("\nFlight code (IATA): {}\nDeparture Airport : {}, "
                  "Arrival Time : {}, Terminal : {}, Gate : {}"
                  .format(flight['flight']['iata'], flight['departure']['airport'],
                          flight['arrival']['actual'], flight['arrival']['terminal'],
                          flight['arrival']['gate']))

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
         for flight in flight_Data['data']:
               print("\nFlight code (IATA) : {}\nDeparture Airport : {}, Departure Time : {}, Estimated Arrival Time : {}, Terminal : {}, Gate : {}"
                     .format(flight['flight']['iata'], flight['departure']['airport'], flight['departure']['actual'],flight['arrival']['estimated'], flight['arrival']['terminal'], flight['arrival']['gate']))
    elif number == '3':
        print("a")
    elif number == '4':
        print("b")
    elif number == '5':
        print(Csock.recv(1024).decode('ascii'))  # Client receives goodbye
        print("\nClient closed\n" + 25 * "=")
        break

    else:
        print(Csock.recv(1024).decode('ascii'))  # When client enters a wrong number

Csock.close()
option = input("Sending number: ")
Csock.send(option.encode('ascii'))
