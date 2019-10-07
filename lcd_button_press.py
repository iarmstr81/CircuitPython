from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
import time
import board
from digitalio import DigitalInOut, Direction, Pull

lcd = LCD(I2CPCF8574Interface(0x27), num_rows= 2, num_cols= 16) #setting up the lcd
lcd.set_cursor_pos(0,0) #where the lcd will start printing 

button = DigitalInOut(board.D2) #setting the pin for button
button.direction = Direction.INPUT
button.pull = Pull.UP #

switch = DigitalInOut(board.D13) #setting the pin for switch
switch.direction = Direction.INPUT
switch.pull = Pull.UP

counter = 0 #counter starts at zero

now = True
later = True
switchValue = True

while True:
        now = button.value
        switchValue = switch.value
        print(str(switchValue)) #print if the switch is up or down
        if now == False and later == True:
            if switchValue: #if switch is up count up
                counter += 1 #go up by 1
            if not switchValue: #if switch is down count down
                counter -= 1 #go down by one
            lcd.set_cursor_pos(0,0) #where the lcd is printing
            lcd.print("button presses: ") 
            lcd.set_cursor_pos(1,0) 
            lcd.print(str(counter)) #print the number of times the button has been pressed
            lcd.print("  ") #to clear the previous number
            time.sleep(0.05)
            now = True
            later = button.value
        time.sleep(.05)



