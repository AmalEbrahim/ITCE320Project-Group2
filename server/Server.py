import json
import socket
import threading
import requests
import os
import time

print("\n********************The Server Has Started******************** \n")
arr_icao = input("\nEnter the airport code (IATA): ").upper()
Ssock_p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Ssock_p.bind(("192.168.43.159", 52499))
Ssock_p.listen(3)


def accept_connection(sock):
    client_name = sock.recv(1025).decode('ascii')
    print("The client -- {} -- is connected".format(client_name))

    while True:
        option = sock.recv(1025).decode('ascii')
        if int(option) == 1:
            params = {
            'access_key': '8b7b55ffde4a7166324303e189733607',
            'arr_iata' : arr_icao,
            'flight_status' : 'landed'
            }
            api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
            api_response = api_result.json()

            Directory = r'C:\Users\amool\PycharmProjects\ITCE320_Project\server'
            if not os.path.exists(Directory):
                os.mkdir(Directory)
            file_path = Directory + '/G2.json'

            file = open(file_path, 'w')
            file.write(json.dumps(api_response, indent=3))  # Saving the retrieved information in a .json file
            file.close()

            with open(file_path, 'rb') as file:
                toSendFile = file.read()  # Reading the content of the file as a preparation for sending
                sock.sendall(toSendFile)
            print("The requested details from {} sent successfully".format(client_name))
        if int(option) == 2:
            params = {
                'access_key': '8b7b55ffde4a7166324303e189733607',
                'dep_iata': arr_icao,
                'min_delay_arr': '0'
            }
            api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
            api_response = api_result.json()

            Directory = r'C:\Users\amool\PycharmProjects\ITCE320_Project\server'
            if not os.path.exists(Directory):
                os.mkdir(Directory)
            file_path = Directory + '/G2.json'

            file = open(file_path, 'w')
            file.write(json.dumps(api_response, indent=3))  # Saving the retrieved information in a .json file
            file.close()
            
            with open(file_path, 'rb') as file:
                toSendFile = file.read()  # Reading the content of the file as a preparation for sending
                sock.sendall(toSendFile)
            print("The requested details from {} sent successfully".format(client_name))




clients = []
while True:
    Ssock_a, sockName = Ssock_p.accept()
    t = threading.Thread(target=accept_connection(Ssock_a))
    t.start()
