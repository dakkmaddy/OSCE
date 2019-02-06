#!/usr/bin/python
#
# Hardcode IP, PORT and fuzzes TFTP filename parameter up to 5000 bytes
# Increments of 25
# so 5000 / 25 this will need 400 passes to complete
#
import socket
import sys
import time

# Hardcode IP and PORT
# Ok, I admit hardcode IP is lame, but the port why bother, who is going to put TFTP on another port, Muts?
# Oh wait...

host = '192.168.100.157'
port = 69

# Buffer is the variable that will be the filename

buffer=["A"]
counter=25

# This is the loop that goes from 25 to 5000, assuming my multiplication is good.
while len(buffer) <=400:
        buffer.append("A"*counter)
        counter=counter+25

for string in buffer:
    print "[-] Hey boo, fuzzing filename %s bytes in TFTP, Check WireShark & Debugger!" % len(string)
    try:
    	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    except:

	print "[-] socket() failed"
	print "[-] wonk wonk wonk wonk"
	sys.exit(1)

    filename = string
    mode = "netascii"
    muha = "\x00\x02" + filename + "\0" + mode+ "\0"
    s.sendto(muha, (host, port))
    time.sleep(1)
