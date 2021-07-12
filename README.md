# Getting Started with RPi Pico
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

## Step 6: The Neopixel Library
In this section, we will be talking about the library. So please refer to the neopixelmatrix.py file. This library was written for a custom-made 9x9 matrix but can be pretty easily used for other matrices with some changes. Below, I have explained all the functions in this library. You will find these functions in ```class NeopixelMatrix```.
### 1. ```__ init__```
Arguments:
> ```Pin```: This argument has to be an integer. It is the pin number where the DIN of the matrix is connected.

If you are using a different matrix:
This function is the initializer for the class and it is written for the the 9x9 matrix. If the dimensions of the matrix are changed, change the spiral numbering because some of the later functions won't work otherwise. Neopixel family has several LEDs with the same communication protocol. The 9x9 matrix I use is made from SK6805.

### 2. ```__set_pattern```
This method sends the data from the array to the actual matrix to make the patterns appear on the matrix.
