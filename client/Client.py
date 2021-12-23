import json
import os
import socket
import sys

print("\n********************The Client Has Started******************** \n")
server_address = ("192.168.43.201", 52499)

Csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Csock.connect(server_address)
my_name = input("Enter client name: ")   # ask the client to enter her name
Csock.send(my_name.encode('ascii'))  # send the UserName to server
arr_icao = input("\nEnter the airport code:").upper()
Csock.send(arr_icao.encode('ascii'))  # send airport code to server

while True:
    # take the input option from the user
    print("\nSelect an Option:\n"
          "1. Display all arrived flights details.\n"
          "2. Display all delayed flights details.\n"
          "3. Display all flights coming from a specific city\n"
          "4. Display all details of particular flight\n"
          "5. Quit.\n")

    number = input("Sending number: ")
    Csock.sendall(number.encode('ascii'))  # send the option number to server
    if int(number) == 1:
        print("All arrived flights : ")
        Directory = r'C:\Users\amool\PycharmProjects\ITCE320_Project\client\client_{}'.format(my_name)
        # create directory if it is not found and save the information inside it
        if not os.path.exists(Directory):
            os.mkdir(Directory)
        file_path = Directory + '/G2.json'

        with open(file_path, 'wb') as file:  # saving information in JSON file in client folder
            recvfile = Csock.recv(1048576)
            file.write(recvfile)

        with open(file_path) as file:
            flight_Data = json.load(file)  # Convert the JSON data into python objects
            for flight in flight_Data["data"]:
                print("\nFlight code (IATA) : {}\nDeparture Airport : {}, Arrival Time : {}, "
                      "Terminal : {}, Gate : {}".format(flight['flight']['iata'],
                                                        flight['departure']['airport'],
                                                        flight['arrival']['actual'],
                                                        flight['arrival']['terminal'],
                                                        flight['arrival']['gate']))

    elif int(number) == 2:
        print("All delayed flights : ")
        Directory = r'C:\Users\amool\PycharmProjects\ITCE320_Project\client\client_{}'.format(my_name)
        # create directory if it is not found and save the information inside it
        if not os.path.exists(Directory):
            os.mkdir(Directory)
        file_path = Directory + '/G2.json'

        with open(file_path, 'wb') as file:  # saving information in JSON file in client folder
            recvfile = Csock.recv(1048576)
            file.write(recvfile)

        with open(file_path) as file:
            flight_Data = json.load(file)  # Convert the JSON data into python objects
            for flight in flight_Data["data"]:
                print("\nFlight code (IATA) : {}\nDeparture Airport : {}, "
                      "Departure Time : {}, Estimated Arrival Time : {}, "
                      "Terminal : {}, Gate : {}".format(flight['flight']['iata'],
                                                        flight['departure']['airport'],
                                                        flight['departure']['actual'],
                                                        flight['arrival']['estimated'],
                                                        flight['arrival']['terminal'],
                                                        flight['arrival']['gate']))

    elif int(number) == 3:
        cityName = input("Enter city code: ").upper()
        Csock.sendall(cityName.encode('ascii'))
        print("All flights coming from {}: ".format(cityName))
        Directory = r'C:\Users\amool\PycharmProjects\ITCE320_Project\client\client_{}'.format(my_name)
        # create directory if it is not found and save the information inside it
        if not os.path.exists(Directory):
            os.mkdir(Directory)
        file_path = Directory + '/G2.json'

        with open(file_path, 'wb') as file:   # saving information in JSON file in client folder
            recvfile = Csock.recv(1048576)
            file.write(recvfile)

        with open(file_path) as file:
            flight_Data = json.load(file)  # Convert the JSON data into python objects
            for flight in flight_Data["data"]:
                print("\nFlight code (IATA) : {}\nDeparture Airport : {}, Departure Time : {}, "
                      "Estimated Arrival Time : {}, Terminal : {}, "
                      "Gate : {}".format(flight['flight']['iata'],
                                         flight['departure']['airport'],
                                         flight['departure']['actual'],
                                         flight['arrival']['estimated'],
                                         flight['arrival']['terminal'],
                                         flight['arrival']['gate']))

    elif int(number) == 4:
        flightNum = input("Enter flight number: ")
        Csock.sendall(flightNum.encode('ascii'))

        print("Details of flight {}".format(flightNum))
        Directory = r'C:\Users\amool\PycharmProjects\ITCE320_Project\client\client_{}'.format(my_name)
        # create directory if it is not found and save the information inside it
        if not os.path.exists(Directory):
            os.mkdir(Directory)
            file_path = Directory + '/G2.json'

            with open(file_path, 'wb') as file:  # saving information in JSON file in client folder
                recvfile = Csock.recv(1035)
                file.write(recvfile)

                with open(file_path) as file:
                    flight_Data = json.load(file)  # Convert the JSON data into python objects
                for flight in flight_Data['data']:
                    print("\nFlight code (IATA) : {},    Date : {},\nDeparture Airport : {}, "
                          "Departure Gate : {}, Departure Terminal : {}, \nArrival Airport : {}, "
                          "Arrival Gate : {}, Arrival Terminal : {}, Status : {}, Scheduled Departure Time: {}, "
                          "Scheduled Arrival Time : {}, Estimated Arrival Time : {}, delay : {}".format(
                        flight['flight']['iata'], flight['flight_date'],flight['departure']['airport'],
                        flight['departure']['gate'], flight['departure']['terminal'],
                        flight['arrival']['airport'], flight['arrival']['gate'],
                        flight['arrival']['terminal'], flight['flight_status'],
                        flight['departure']['scheduled'], flight['arrival']['scheduled'],
                        flight['arrival']['estimated'], flight['arrival']['delay']))

    elif int(number) == 5:
        print(Csock.recv(1024).decode('ascii'))  # Client receives goodbye
        print("\nClient closed\n" + 25 * "=")
        Csock.close()
        break

    else:
        continue  # When client enters a wrong number

sys.exit()
