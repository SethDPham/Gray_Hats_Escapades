#nc 107.170.192.50 1900

import socket

s = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)

s.connect(("107.170.192.50", 1900))
srvMessage = s.recv(10000)
print(srvMessage)

connected = True
reps = 0
print connected

s.send("1")

while reps < 10000:
	line = s.recv(10000)
	input = line.split()
	print "Received from server: " + line
	if(input[1] == "+"):
		output = int(input[0]) + int(input[2])
	elif (input[1] == "-"):
		output = int(input[0]) - int(input[2])
	print input
	print("before")
	print output

	s.send(str(output))

	reps+=1
	print "reps: " + str(reps) 
	#connected = False
	#print("connected set to False")

print ("end of program")

