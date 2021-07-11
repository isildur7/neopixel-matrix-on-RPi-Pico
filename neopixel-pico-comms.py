# Talk to a computer and change illumination pattern
# on the neopixel matrix

from neopixelmatrix import NeopixelMatrix
import utime
import sys
import select

# this code assumes that you don't want to break the system
# it will not provide too many guarantees against bad inputs

while True:
    
    if select.select([sys.stdin],[],[],0)[0]:
        utime.sleep(2)
        ch = sys.stdin.readline()
        while not (str(ch).startswith("INIT PIN ")):
            print("Unrecognized command!\n")
            if select.select([sys.stdin],[],[],0)[0]:
                ch = sys.stdin.readline()
        
        pin = int(str(ch).split(" ")[2][:-1])
        print("LED array at GPIO {}\n".format(pin))
        neo = NeopixelMatrix(pin)

        #neo.fill(0x734830)
        
        while True:
            if select.select([sys.stdin],[],[],0)[0]:
                ch = sys.stdin.readline()
                command = str(ch)
                
                if command.startswith("ALL OFF"):
                    print("Turning matrix off\n")
                    neo.allOff()
                    
                elif command.startswith("FILL27"):
                    side = command.split(" ")[1]
                    color = int(command.split(" ")[2][:-1], 0)
                    print("{} half turned on with color {}".format(side, hex(color)))
                    neo.fill27(side, color)
                    
                elif command.startswith("FILL18"):
                    side = command.split(" ")[1]
                    color = int(command.split(" ")[2][:-1], 0)
                    print("{} half turned on with color {}".format(side, hex(color)))
                    neo.fill18(side, color)
                
                elif command.startswith("FILL"):
                    color = int(command.split(" ")[1][:-1], 0)
                    print("Filling the matrix with color {}".format(hex(color)))
                    neo.fill(color)
                
                elif command.startswith("RING"):
                    radius = int(command.split(" ")[1], 0)
                    color = int(command.split(" ")[2][:-1], 0)
                    print("Ring {} turned on with color {}".format(radius, hex(color)))
                    neo.ring(radius, color)
                
                elif command.startswith("CIRCLE"):
                    radius = int(command.split(" ")[1], 0)
                    color = int(command.split(" ")[2][:-1], 0)
                    print("Circle {} turned on with color {}".format(radius, hex(color)))
                    neo.fillCircle(radius, color)
                
                elif command.startswith("HALF"):
                    side = command.split(" ")[1]
                    color = int(command.split(" ")[2][:-1], 0)
                    print("{} half turned on with color {}".format(side, hex(color)))
                    neo.fillHalf(side, color)
                    
                    
                elif command.startswith("KEY"):
                    key = int(command.split(" ")[1], 0)
                    color = int(command.split(" ")[2][:-1], 0)
                    print("LED {} turned on with color {}".format(key, hex(color)))
                    neo[key] = color
                
                elif command.startswith("SPIRALKEY"):
                    key = int(command.split(" ")[1], 0)
                    color = int(command.split(" ")[2][:-1], 0)
                    print("LED {} (spiral) turned on with color {}".format(key, hex(color)))
                    neo.setSpiralIndex(key, color)
                    
                else:
                    print("'{}' is an unrecognized command".format(command))
                
