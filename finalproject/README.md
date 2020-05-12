# **Embedded Linux Final Project**
I chose to create a weather system with my Raspberry Pi for my final project.
## **Equipment**
The materials and equipment I used to create this include:
* Raspberry Pi
* GPIO board
* GPIO board to Raspberry Pi cable connector
* DHT11 Temperature & Humidity Sensor Module
* BMP180 Digital Barometric Pressure Sensor Module
* Photosensitive Light Sensor Module
* Water Level Sensor Module
* Jumper wires
## **Wiring**
I used quite a lot of jumper wires for my project because I was using four sensors most of which have inputs, outputs, and grounds.
Each sensor required three wires (MBP180 requires four, but we'll get there) to get it connected. I'll go through each sensor step by step, and you can reference the image any time you'd like for extra assistance. First
thing to do however, since there are four sensors and only two 3v3 voltage outputs on the GPIO connector board, take a small red jumper wire, plug it into the 3v3 outlet, and then connect the other end to the first output spot in the red plus (+) row. 
We will connect each sensor to this red plus row to give them 3v3 voltage power.
1. **Water Level Sensor Module**
I used the jumper wires that have pins on and connectors on the other end. Since this is a water sensor that will be detecting rain, this will make it easier to stick the
sensor out of the window without ruining your weather system
	1. Take a jumper wire (one specified above) connect it to the '-' plug and pin it into a ground 'GND'
	1. With another jumper wire connect it to the '+' plug on the sensor and pin it in the red plus row on the board.
	1. The last wire gets connected to the 'S' plug and gets pinned into 'GPIO22' which is pin number 22 when coding the weather system.
1. **MBP180 Digital Barometric Pressure Sensor Module**
For the remaining three sensors I used the regular jumper wires that have pins on both sides of the wire. I also just plugged these sensor modules into the GPIO
board itself.
	1. Plug the sensor into the GPIO board
	1. With a jumper wire, plug the pin into the spot infront of the sensor labeled '3.3' and plug the other end into the red plus row on the board
	1. Plug another wire infront of the sensor labeled 'SDA' and put the other end into the GPIO connecter slot labeled 'SDA1'
	1. Another wire goes infornt of 'SCL' and into 'SCL1' on the connector
	1. The last wire for this sensor goes into 'GND' and likewise into a 'GND' slot on the connector.
	1. Connecting wires into the spot labeled 'VCC' wont be necessary so don't worry about that.
1. **DHT11 Temperature & Humidity Sensor Module**
	1. Plug the sensor into the GPIO board
	1. Use a jumper wire and plug one end of the pin into the spot infront of the sensor that is labeled 'VCC' and plug the other end into into a spot in the red plus row on the GPIO board
	1. Another jumper wire is used to connect the spot on the sensor labeled 'DATA' to 'GPIO17' which is GPIO pin number 17 to be used later in the code
	1. The last jumper wire connects the sensor output labeled 'GND' to a 'GND' spot on the GPIO connector
1. **Photosensitive Light Sensor Module**
	1. Plug the light sensor into the GPIO board
	1. This sensor has four outputs like the MPB180 sensor, only use the three labeled 'VCC', 'GND', and 'DO'
	1. Using a jumper wire pin 'VCC' on the sensor to a spot in the red plus row on the GPIO board
	1. Another wire is used to connect 'GND' to a 'GND' spot on the connector
	1. Lastly connect 'DO' to 'GPIO18' on the connector. This will be the light sensors pin number, 18.
![full setup](/Users/lukedole/Desktop/IMG_1223.jpeg)
