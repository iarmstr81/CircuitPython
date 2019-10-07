import board
from digitalio import DigitalInOut, Direction, Pull
import time

button = DigitalInOut (board.D7)
button.direction = Direction.INPUT
button.pull = Pull.UP
#making now and later functions
now = True
later = True
lastTime = 0
counter = 0 

while True:
    nowT = time.monotonic() #time.monotonic is the amount of time since it was last checked
    now = button.value

    if nowT - 4 >= lastTime: # if you haven't checked in under 4 print that is has been interrupted and how many times it has
        print ("interrupted")
        print(counter)
        #time.sleep(.05)
        lastTime = time.monotonic() # set the time back to zero

    if now == False and later == True: #when photointerrupter is interrupted making now false and later true increase counter
        counter += 1 #count up by one
        #time.sleep(.05)
    later = now 