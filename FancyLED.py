import digitalio #pylint: disable-msg=import-error
import time 
import random

class fancyLED:
    
    def __init__(self,p1,p2,p3):
        print("setting pins")
        self.X1 = digitalio.DigitalInOut(p1)
        self.X1.direction = digitalio.Direction.OUTPUT
        self.Y1 = digitalio.DigitalInOut(p2)
        self.Y1.direction = digitalio.Direction.OUTPUT
        self.Z1 = digitalio.DigitalInOut(p3)
        self.Z1.direction = digitalio.Direction.OUTPUT

    def alternate(self):
        print("alternate")
        self.X1.value = True
        self.Y1.value = False
        self.Z1.value = True
        time.sleep(.5)
        self.X1.value = False
        self.Y1.value = True
        self.Z1.value = False
        time.sleep(.5)
        self.X1.value = False
        self.Y1.value = False
        self.Z1.value = False
    
    def blink(self):
        print("blink")
        self.X1.value = True
        self.Y1.value = True
        self.Z1.value = True
        time.sleep(.5)
        self.X1.value = False
        self.Y1.value = False
        self.Z1.value = False
        time.sleep(.5)
        self.X1.value = False
        self.Y1.value = False
        self.Z1.value = False

    def chase(self):
        print("chase")
        self.X1.value = True
        self.Y1.value = False
        self.Z1.value = False
        time.sleep(.5)
        self.X1.value = False
        self.Y1.value = True
        self.Z1.value = False
        time.sleep(.5)
        self.X1.value = False
        self.Y1.value = False
        self.Z1.value = True
        time.sleep(.5)
        self.X1.value = False
        self.Y1.value = False
        self.Z1.value = False
        

    def sparkle(self):
        for whatever in range (0,50):
            print("sparkle")
            n = random.randint(1,3)
            print (n)
            if n == 1:
                self.X1.value = True
                self.Y1.value = False
                self.Z1.value = False

            elif n == 2:
                self.X1.value = False
                self.Y1.value = True
                self.Z1.value = False
            elif n == 3:
                self.X1.value = False
                self.Y1.value = False
                self.Z1.value = True
            time.sleep(.05)
            self.X1.value = False
            self.Y1.value = False
            self.Z1.value = False
            

       
