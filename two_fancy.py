from FancyLED import fancyLED

board.D2 = a1
board.D3= b1
board.D4 = c1
board.D5 = a2
board.D6 = b2
board.D7 = c2

fancy1 = fancyLED(2,3,4)
fancy2 = fancyLED(5,6,7)

while True:
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()