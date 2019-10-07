import digitalio #pylint: disable-msg=import-error
import time 
import random

class fancyLED:
    
    def __init__(self,p1,p2,p3):
        print("setting pins")
        self.X1 = digitalio.DigitalInOut(p1)
        self.X1.direction = digitalio.Direction.OUTPUT #turning led on
        self.Y1 = digitalio.DigitalInOut(p2)
        self.Y1.direction = digitalio.Direction.OUTPUT #turning led on
        self.Z1 = digitalio.DigitalInOut(p3)
        self.Z1.direction = digitalio.Direction.OUTPUT #turning led on

    def alternate(self): # two leds on at same time other off and flip 
        print("alternate")
        self.X1.value = True #led on
        self.Y1.value = False #led off
        self.Z1.value = True #led on
        time.sleep(.5)
        #opposite of ^
        self.X1.value = False 
        self.Y1.value = True
        self.Z1.value = False
        time.sleep(.5)
        # all led off to clear leds on
        self.X1.value = False 
        self.Y1.value = False
        self.Z1.value = False
    
    def blink(self): # all led flash on at the sametime and off at the sametime
        print("blink")
        #all leds on
        self.X1.value = True 
        self.Y1.value = True
        self.Z1.value = True
        time.sleep(.5)
        #all leds off
        self.X1.value = False
        self.Y1.value = False
        self.Z1.value = False
        time.sleep(.5)
        #clear all leds
        self.X1.value = False
        self.Y1.value = False
        self.Z1.value = False

    def chase(self): #first led on then the next then the last
        print("chase")
        #first led on rest off
        self.X1.value = True
        self.Y1.value = False
        self.Z1.value = False
        time.sleep(.5)
        #second led on first and last off
        self.X1.value = False
        self.Y1.value = True
        self.Z1.value = False
        time.sleep(.5)
        #third led on first and second off
        self.X1.value = False
        self.Y1.value = False
        self.Z1.value = True
        time.sleep(.5)
        #clear all leds
        self.X1.value = False
        self.Y1.value = False
        self.Z1.value = False
        
    def sparkle(self): #random led turn on 
        for whatever in range (0,50): #turn a random led on 50 times
            print("sparkle")
            n = random.randint(1,3) #pick a random led 1-3
            print (n)
            if n == 1: #if 1 turn on first led
                self.X1.value = True
                self.Y1.value = False
                self.Z1.value = False

            elif n == 2: #if 2 turn on second led
                self.X1.value = False
                self.Y1.value = True
                self.Z1.value = False

            elif n == 3: #if 3 turn o third led
                self.X1.value = False
                self.Y1.value = False
                self.Z1.value = True
            time.sleep(.05)
            #clear all leds
            self.X1.value = False
            self.Y1.value = False
            self.Z1.value = False
            

       
