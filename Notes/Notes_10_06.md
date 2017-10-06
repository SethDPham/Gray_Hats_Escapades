### 10/06/2017

## Topics
* Basic Networking
* Netcat
* Apache Webserver

### OSI Model
	Upper
		Application  (HTTP, FTP)
		Presentation (JPEG, GIF)
		Session 	 (WinSock, AppleTalk)
	Lower
		Transport    (TCP, UDP) <-- PortNumber
		Network 	 (IP)
		Data Link    (Ethernet, ATM)
		Physical     (Ethernet, Token Ring)

### Finding ip address
    ip a

### Netcat
* HTTP Port 80
* SSH Port 22
* Create a shell to interact with the webserver
        # nc -nvlp <port number>
        # nc -nvlp 8080
    Hosted a netcat port anyone can access
* For an administrative command
        # nc nvlp 8080 -e /bin/bash
    Anyone that connects, can execute bash commands on the computer
* To connect
        # nc <ip address> <port number>

### Important info
    # /etc/shadow
* is a file that stores passwords
* passwords are in encrypted format


	# netstat -antp
* shows all the ports and connections currently

### Nmap
    nmap  <ip address>
* Scans which ports are open
	* You can specify the port range

### Socket Practice
    nc 107.170.192.50 1900
Practice with sockets on the LittleKoala network