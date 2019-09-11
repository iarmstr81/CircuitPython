import board
from digitalio import DigitalInOut, Direction, Pull
import time

button = DigitalInOut (board.D7)
button.direction = Direction.INPUT
button.pull = Pull.UP
now = True
later = True
lastTime = 0
counter = 0

while True:
    nowT = time.monotonic()
    now = button.value

    if nowT - 4 >= lastTime:
        print ("interrupted")
        print(counter)
        #time.sleep(.05)
        lastTime = time.monotonic()

    if now == False and later == True:
        counter += 1
        #time.sleep(.05)
    later = now