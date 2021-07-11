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

Try writing some code and saving it on the Pico, also try to save it as main.py.
