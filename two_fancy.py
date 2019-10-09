import board #pylint: disable-msg=import-error
import digitalio #pylint: disable-msg=import-error
from FancyLED import fancyLED

#setting each led to a pin
a1 = board.D2 
b1 = board.D3
c1 = board.D4 
a2 = board.D5 
b2 = board.D6
c2 = board.D7

print("fancy LED!")

fancy1 = fancyLED(2,3,4) #certain leds are fancy1
fancy2 = fancyLED(5,6,7) #the other leds are fancy2

while True:
    #functions that will happen
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()