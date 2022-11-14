# Ticketing-Application
Python Flask flight ticket api gateway creation

![resim](https://user-images.githubusercontent.com/40759486/182633350-52ff5b89-012e-49cb-a0b6-213443a83faa.png)

![resim](https://user-images.githubusercontent.com/40759486/182633383-165e3fe0-794e-41b4-a000-388df86b8982.png)


Using the api, you can use web, mobile, IoT, etc. we can serve all front-end points

![resim](https://user-images.githubusercontent.com/40759486/182634730-4ba314b3-f3d8-45a6-ab01-3d86cd01ce10.png)


But sometimes works get complicated and a single API is not enough. 
APIs must communicate with each other and they must work as sub-processes of a process.

Ticketing applications are an important example of this.

Worldwide booking.com, skyscanner.com, ratehawk.com etc are the best examples of this.
In Turkey, biletal.com, enuygun.com, turna.com, ucuzbilet.com etc.

![fligsth_servers](https://user-images.githubusercontent.com/40759486/182635865-26476b73-e649-4c0a-bbd6-ca6a839d2c16.png)



The ticketing process is based on 3 main basis. /search, /revalidate, /createPnr . 

As expected, the /search section has a structure that searches the desired number of adult/child passengers for different requests, such as listing flights at desired intervals, direct flights, connecting flights, connecting flights and round-trip flights, and returns this quickly.

Worldwide services such as Saber, THY, Amadeus, IATA, DUFFEL give you flight data. However, if you want to make a good practice and suggest many alternative companies to the user who wants to do ticketing, you should use the above services and local country services.

That means too many services and you have to manage that too. This API-GATEWAY is available in AWS, GCP, Azure options.


![resim](https://user-images.githubusercontent.com/40759486/182638433-e37dbd88-8adc-4bd4-a764-c406e2417c4c.png)


/revalidate part is a method of guaranteeing that the selected flight in the flight search is still on sale at the time of purchase.

/createPNR, The last step of the /createPnr ticketing process is to create the pnr. PNR is your trip code. Check-in vs. It is possible to detect your ticket with pnr in transactions. Passenger information is usually taken here.
