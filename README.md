# RPi Pico Neopixel Instructions
![RPi Pico](https://pbs.twimg.com/media/EvsYoiOVIAQ0hfh?format=jpg&name=large)

## Step 1: Installing Thonny
Go to [this link](https://thonny.org/) and download thonny. Install it with the default settings. After installation, you can also go to Tools > Options... > Theme & Font to set the appearance and make it comfortable for you.

## Step 2: Installing Micropython Firmware onto the RPi Pico
To run micropython on our RPi Pico, we need to install some firmware on it. We can use thonny for this too. To do this, in thonny go to Tools > Options... In options, go to the interpreter tab. At this point, you will also have to plug in your RPi Pico using a USB cable so keep it handy. In this tab, in the bottom right corner will be an option called "Install or update firmware". Click on that and follow the instructions. 

![Firmware Installation](https://github.com/isildur7/neopixel-matrix-on-RPi-Pico/blob/main/Screenshot%202021-07-11%20225353.jpg?raw=true)

## Step 3: Play Around!
> The Pico runs a lightweight interpreter called REPL (Read Evaluate Print Loop). It allows us to write commands and execute them on the Pico in real time just like command line.

So, just try typing ```print("Hello World!")``` in the shell and see the output. That instruction was run on the RPi Pico! :partying_face:

## Step 4: Come Out of Your Shell
While the shell and REPL is great for interacting with the Pico, we want to write big programs and also save them somewhere. We write these programs in the editor above the shell. After we write a piece of code in the editor, we want to save the it. For that you have two options:
1. Save the code on your computer and run it on the Pico when you want to. 
2. The probably more interesting way is to save the code on the RPi Pico itself. You can store multiple files of code on the RPi Pico. This can also be done by dragging and dropping as RPi Pico shows up as an external drive to your computer.
Note:
> If you want a certain piece of code to run automatically whenever you connect the Pico to power, save that code on the Pico with the filename "main.py".

Small Homework: Try writing some code and saving it on the Pico, also try to save it as main.py.

![Code Example](https://github.com/isildur7/neopixel-matrix-on-RPi-Pico/blob/main/Screenshot%202021-07-11%20225544.jpg?raw=true)

In this image you can see a program called "Hello World.py" which is just a simple program I have saved on my pico and you can also see the output I have got from the Pico in the shell.

## Step 5: Connecting "Peripherals" (aka LEDs)
The RPi Pico has a lot of GPIO pins with different communication protocols. You can use these pins to connect stuff like LEDs, sensors and other fancy stuff. The image given below shows the pinout of the Pico and it will help you identify the pin numbers to connect stuff.

![RPi Pico Pinouts](https://cdn-shop.adafruit.com/1200x900/4883-06.png)

## The Neopixel Library
The ```neopixelmatrix.py``` is the library file you can save on Pico and import in your code. This library was written for a custom-made 9x9 matrix but can be pretty easily used for other matrices with some changes. Start by initializing the matrix with the GP pin number to which DIN is connected. The initializer for the class is written for the the 9x9 matrix. If the dimensions of the matrix are changed, change the spiral numbering because some of the later functions won't work otherwise. Neopixel family has several LEDs with the same communication protocol. The 9x9 matrix I use is made from SK6805. Other functions are explained using comments in the ```neopixelmatrix.py``` file.
```
from neopixelmatrix import NeopixelMatrix

neo = NeopixelMatrix(pin=0)
neo.fill(0x457134)
neo.allOff()
neo.setSpiralIndex(52, 0x941350)
neo.ring(2, 0x135945)
neo.fillHalf("T", 0x9A845E)
neo.fill18("B", 0x9A845E)
neo.allOff()
```

![9x9 LED Matrix](https://github.com/isildur7/neopixel-matrix-on-RPi-Pico/blob/main/20210712062249_IMG_2791.JPG?raw=true)

## Serial Communication
We will be communicating with our matrix using serial commands. For this section, refer to the file neopixel-pico-comms.py. Below are the serial commands and their functions from ```neopixel-pico-comms.py```. You will need to copy this file onto the Pico as ```main.py```. Also copy the ```neopixelmatrix.py``` onto Pico as it is.


1. ```INIT PIN <pinNum>```:

This command initializs our program. Type the pin number at which your DIN is connected after INIT PIN and hit enter (for example ```INIT PIN 0``` if you are connected at GP0). If everything goes right, you should see a message like ```LED array at GPIO <pinNum>```. LED color inputs for all the commands *must be* the hex codes (entered as 0xRRGGBB).

2. ```ALL OFF```:

This command turns all the LEDs on the matrix OFF.

3. ```FILL27 <side> <color>```:

Two more quantities have to be given with this command. The side and the color (in that order). The side can be one of T, B, R, L i.e. Top, Bottom, Right, Left. The color has to given in the format 0x an then the hex code (this applies to all the functions which have a color input). So an example would be ```FILL27 T 0x123123```. This will turn on the top 27 LEDs on the matrix with the color 123123.

4. ```FILL18 <side> <color>```:

This command is very similar to FILL27. It requires the same inputs but the difference is that it turns ON only 18 LEDs instead of 27.

5. ```FILL <color>```:

This command fills the entire matrix with the color you input with it.

6. ```RING <radius> <color>```:

This command turns ON LEDs in form of a ring. It takes the inputs radius and color (in that order). The minimum radius is 0 and the maximum radius can be 3.

7. ```CIRCLE <radius> <color>```:

This command turns ON LEDs in form of a circle. It takes the inputs radius and color (in that order). The minimum radius is 0 and the maximum radius can be 4.

8. ```HALF <side> <color>```:

This turns ON half of the LED matrix. It also takes two inputs side and color just like FILL27.

9. ```KEY <index> <color>```:

This turns ON a particular LED. It takes the LED index and the color as input (in that order). The numbering of the LEDs starts from a corner and snakes downward. Note that the first LED is numbered 0.

![Key](https://github.com/isildur7/neopixel-matrix-on-RPi-Pico/blob/main/Inked20210712062249_IMG_2791_LI.jpg?raw=true)

10. ```SPIRALKEY <index> <color>```:

Just like ```KEY``` this too turns ON a particular LED. It takes the LED index and the color as input (in that order). The numbering of the LEDs starts from the center and spirals outwards. Note that the first LED is numbered 0.

![Spiralkey](https://github.com/isildur7/neopixel-matrix-on-RPi-Pico/blob/main/Inked20210712062249_IMG_2791_LI2.jpg?raw=true)

## How to actually do the communication
There are two ways: 
### Using a Serial Monitor like the Arduino Serial Monitor
#### Step 1:
Save the ```neopixel-pico-comms.py``` file as ```main.py``` on your Pico so it runs automatically when you connect your Pico to power. Also save ```neopixelmatrix.py``` on your Pico. Assemble the matrix circuit, connect the Pico to your computer.
#### Step 2: 
Open your Arduino IDE, go to tools, select the right COM port and then open the serial monitor.
#### Step 3:
Set the baud rate to 115200 and select Carriage Return ending.

![Serial Monitor](https://github.com/isildur7/neopixel-matrix-on-RPi-Pico/blob/main/Screenshot%202021-07-12%20171104.jpg?raw=true)
#### Step 4: 
Type INIT PIN followed by your pin number to initialize and then you can type in any commands you want after.

### With another program or script
Using the protocol above you can open a serial channel and transmit commands to the Pico through another device. For example, using the PySerial library a script could look like:
```
import serial
import time

COM_PORT = 'COM7'
BAUD_RATE = 115200
GP_pin = 0

# initialize the LED comm port and the array
LEDport = serial.Serial(COM_PORT, BAUD_RATE)
LEDport.write(("INIT PIN "+str(GP_pin)+"\r").encode("ascii"))
time.sleep(0.5)
LEDport.write(("ALL OFF\n").encode("ascii"))

# brightfield illumination
LEDport.write(("CIRCLE 1 0xFFFFFF\r").encode("ascii"))
time.sleep(1)
LEDport.write(("ALL OFF\n").encode("ascii"))

# green left half  
LEDport.write(("FILL24 L 0x00FF00\r").encode("ascii"))
time.sleep(1)
LEDport.write(("ALL OFF\n").encode("ascii"))
```
