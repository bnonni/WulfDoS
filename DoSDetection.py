#!/usr/bin/env python3

import socket
import struct

from datetime import datetime

# Packet sniffing on Linux
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)

# USE THIS FOR WIN OR MAC: socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)

dict = {}

file_txt = open("attack_DDoS.txt", 'a')
t1 = str(datetime.now())

file_txt.writelines(t1)
file_txt.writelines("\n")

No_Of_IPs = 15
R_No_Of_IPs = No_Of_IPs + 10

while True:
    pkt = s.recvfrom(2048)
    ipheader = pkt[0][14:34]
    ip_hdr = struct.unpack("!8sB3s4s4s", ipheader)
    IP = socket.inet_ntoa(ip_hdr[3])
    print("The source of IP: ", IP)

if dict.has_key(IP):
    dict[IP] = dict[IP] + 1
    print(dict[IP])

if(dict[IP] > No_Of_IPs) and (dict[IP] < R_No_Of_IPs):
    line = "DDoS attack is Detected: "
    file_txt = writelines(line)
    file_txt = writelines(IP)
    file_txt = writelines("\n")
else:
    dict[IP] = 1
