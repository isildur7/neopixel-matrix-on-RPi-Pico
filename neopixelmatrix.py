# Neopixel matrix library for RPi Pico
# Amey Chaware
# May 2021

import array, utime
from machine import Pin
import rp2
from rp2 import PIO, StateMachine, asm_pio

@asm_pio(sideset_init=PIO.OUT_LOW, out_shiftdir=PIO.SHIFT_LEFT,
autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    label("bitloop")
    out(x, 1) .side(0) [T3 - 1]
    jmp(not_x, "do_zero") .side(1) [T1 - 1]
    jmp("bitloop") .side(1) [T2 - 1]
    label("do_zero")
    nop() .side(0) [T2 - 1]
    return

def RGB_to_GRB(rgb):
    R = rgb & 0xFF0000
    G = rgb & 0xFF00
    B = rgb & 0xFF
    return (R >> 8) | (G << 8) | B
    
def GRB_to_RGB(grb):
    G = grb & 0xFF0000
    R = grb & 0xFF00
    B = grb & 0xFF
    return (G >> 8) | (R << 8) | B

class NeopixelMatrix:
    """
    Object to control a Neopixel LED matrix.
    Multiple patterns and spiral indexing is available.
    """
    def __init__(self, pin=0):
        """
        Initializer for the class, needs only global brightness.
        Assumes that we are using one 9x9 Neopixel matrix. Neop-
        ixel family has several LEDs with the same communication
        protocol. The 9x9 matrix I use is made from SK6805.
        
        Arguments -
        pin  :  integer, pin number for a DIN
        """
        # pretty much hardcoded for a 9x9 matrix
        # if that changes, change spiral numbering
        # and unfortunately will need to modify all
        # functions coming after allOff to a 
        # varying degree
        self.numLED = 81
        
        # Create the StateMachine with the ws2812 program, outputting on the given pin.
        self.sm = StateMachine(0, ws2812, freq=8000000, sideset_base=Pin(pin))
        self.sm.active(1)
        
        # array to store the LED data, for all practical purposes this is the matrix.
        # initialize the matrix to have zero color values everywhere
        # each element of the array is an unsigned int
        # the format is GRB (MSB -> LSB)
        self.led_ar = array.array("I", [0 for _ in range(self.numLED)])
        
        # Look up table for spiral pattern
        # My board has a snake-like (adjacent rows go in opposite directions) addressing pattern,
        # change this if yours differs. Also change 'T' and 'B' sections of half, 27 and 18 fill
        # functions
        self.spiral = [40, 41, 48, 49, 50, 39, 32, 31, 30, 29, 42, 47, 60, 59, 58, 57, 56, 51, 38,\
                       33, 20, 21, 22, 23, 24, 25, 28, 43, 46, 61, 64, 65, 66, 67, 68, 69, 70, 55, \
                       52, 37, 34, 19, 16, 15, 14, 13, 12, 11, 10, 9, 26, 27, 44, 45, 62, 63, 80, \
                       79, 78, 77, 76, 75, 74, 73, 72, 71, 54, 53, 36, 35, 18, 17, 0, 1, 2, 3, 4, \
                       5, 6, 7, 8]
        
    def __set_pattern(self):
        """
        private method, sends data from array to the actual matrix to set it
        """
        # shift data by 8 bits to send only the 24 required bits)
        self.sm.put(self.led_ar, 8)
        return
    
    def __getitem__(self, key):
        """
        implementing [] operator access to LED array. self[key] will return
        color value of the LED number key as a hex code.
        """
        return hex(self.GRB_to_RGB((led_ar[key]) & 0xFFFFFF))
    
    def __setitem__(self, key, value):
        """
        implementing [] operator access to LED array. value is treated as a hex
        color code and LED number key is set to that color value.
        """
        if key < 0 or key > 81:
            raise IndexError("LED index out of range")
        self.led_ar[key] = RGB_to_GRB(int(value))
        self.__set_pattern()
        return
    
    def getSpiralIndex(self, key):
        """
        Fetch the LED color value at location key in the spiral pattern
        """
        return hex(GRB_to_RGB((self.led_ar[self.spiral[key]]) & 0xFFFFFF))
    
    def setSpiralIndex(self, key, value):
        """
        Set the LED color value at location key in the spiral pattern to the given
        hex code
        """
        #print(len(self.spiral))
        self.led_ar[self.spiral[key]] = RGB_to_GRB(int(value))
        self.__set_pattern()
        return
    
    def fill(self, color):
        """
        Set all the LEDs to given hex color
        """
        for i in range(self.numLED):
            self.led_ar[i] = RGB_to_GRB(int(color))
        
        self.__set_pattern()
        return
    
    def allOff(self):
        """
        turn all LEDs off
        """
        for i in range(self.numLED):
            self.led_ar[i] = 0
        
        self.__set_pattern()
        return
    
    def fillCircle(self, radius, color):
        """
        Fill up a 'circle' of LEDs (it fills up a square lol) of a given
        radius. Radius is not given in a distance metric, but rather as
        how many unique rings are inside the circle. So, for the 9x9 LED
        array, the radius is from 0 to 4 with 4 filling up the entire array.
        Arguments:
        radius           : Radius from 0 to 4
        color            : should be colour you want for the LED as either an int-hex.
        Returns:
        None
        """
        # number of LEDs 
        LED_in_radius = [1, 9, 25, 49, 81]
        for i in range(LED_in_radius[radius]):
            self.led_ar[self.spiral[i]] = RGB_to_GRB(int(color))
        self.__set_pattern()
        return
    
    def ring(self, radius, color):
        """
        Fill up a ring of LEDs (it fills up a square ring lol) of a given
        radius. Radius is not given in a distance metric, but rather as
        how many unique rings are inside the circle. So, for the 8x8 LED
        array, the radius is from 0 to 3 with 3 turning on the outermost ring.
        Arguments:
        radius           : Radius from 0 to 3
        color            : should be colour you want for the LED as either an int-hex or rgb.
        Returns:
        None
        """
        LED_in_radius = [0, 1, 9, 25, 49, 81]
        for i in range(LED_in_radius[radius], LED_in_radius[radius+1]):
            self.led_ar[self.spiral[i]] = RGB_to_GRB(int(color))
        self.__set_pattern()
        return
    
    def fillHalf(self, side, color):
        """
        turn on half of the array with given color
        Arguments:
        color       : should be colour you want for the LED as either an int-hex or rgb.
        side        : string, 'T','B','R','L' for the top/bottom/right/left respectively
        Returns:
        None
        """
        if side == 'L':
            for i in range(36):
                self.led_ar[i] = RGB_to_GRB(int(color))
        
        elif side == 'R':
            for i in range(45,81):
                self.led_ar[i] = RGB_to_GRB(int(color))
                
        elif side == 'T':
            for i in range(75,0,-18):
                for j in range(i,max(-1, i-8), -1):
                    self.led_ar[j] = RGB_to_GRB(int(color))  
        
        elif side == 'B':
            for i in range(5,80,18):
                for j in range(i,min(81, i+8)):
                    self.led_ar[j] = RGB_to_GRB(int(color))      

        else:
            raise IOError("wrong side parameter, choose either 'L','R','T','B'")
        
        self.__set_pattern()
        return
    
    def fill27(self, side, color):
        """
        turn on 27 leds (3 rows) of the array with given color
        Arguments:
        color       : should be colour you want for the LED as either an int-hex or rgb.
        side        : string, 'T','B','R','L' for the top/bottom/right/left respectively
        Returns:
        None
        """
        if side == 'L':
            for i in range(27):
                self.led_ar[i] = RGB_to_GRB(int(color))
        
        elif side == 'R':
            for i in range(54,81):
                self.led_ar[i] = RGB_to_GRB(int(color))
        
        elif side == 'T':
            for i in range(74,0,-18):
                for j in range(i,max(-1, i-6), -1):
                    self.led_ar[j] = RGB_to_GRB(int(color))
        
        elif side == 'B':
            for i in range(6,80,18):
                for j in range(i,min(81, i+6)):
                    self.led_ar[j] = RGB_to_GRB(int(color))      

        else:
            raise IOError("wrong side parameter, choose either 'L','R','T','B'")
        
        self.__set_pattern()
        return
    
    def fill18(self, side, color):
        """
        turn on 18 leds (2 rows) of the array with given color
        Arguments:
        color       : should be colour you want for the LED as either an int-hex or rgb.
        side        : string, 'T','B','R','L' for the top/bottom/right/left respectively
        Returns:
        None
        """
        if side == 'L':
            for i in range(18):
                self.led_ar[i] = RGB_to_GRB(int(color))
        
        elif side == 'R':
            for i in range(63, 81):
                self.led_ar[i] = RGB_to_GRB(int(color))
        
        elif side == 'T':
            for i in range(73,0,-18):
                for j in range(i,max(-1, i-4), -1):
                    self.led_ar[j] = RGB_to_GRB(int(color))
        
        elif side == 'B':
            for i in range(7,80,18):
                for j in range(i,min(81, i+4)):
                    self.led_ar[j] = RGB_to_GRB(int(color))       

        else:
            raise IOError("wrong side parameter, choose either 'L','R','T','B'")
        
        self.__set_pattern()
        return
        