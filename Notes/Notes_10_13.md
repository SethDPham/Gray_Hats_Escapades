# Gray Hats
### 10/13/17
### BotNets

### Objective
* To make the client pull request from the server look like client code
* The server webpage has python code embedded that will be ran by the client
* Since the client pulls the code to run on their side, it looks like the code was request client side, not server


	** SNEAKY **

### C2
* Webserver parses commands for the other computers to execute

### Start server


		service apache2 start
		service apache2 status

### Index File


		localhost index.html ---> /var/www/html
		modify to run python code

### Scraping an HTML Page


	/etc/apache2
	created a client.py to scrape html pages