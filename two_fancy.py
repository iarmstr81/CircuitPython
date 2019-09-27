import board #pylint: disable-msg=import-error
import digitalio #pylint: disable-msg=import-error
from FancyLED import fancyLED

a1 = board.D2 
b1 = board.D3
c1 = board.D4 
a2 = board.D5 
b2 = board.D6
c2 = board.D7

fancy1 = fancyLED(2,3,4)
fancy2 = fancyLED(5,6,7)

while True:
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()