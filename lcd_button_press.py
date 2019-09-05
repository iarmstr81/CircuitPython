from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
import time
import board
from digitalio import DigitalInOut, Direction, Pull

lcd = LCD(I2CPCF8574Interface(0x27), num_rows= 2, num_cols= 16)
lcd.set_cursor_pos(0,0)

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP

switch = DigitalInOut(board.D13)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

counter = 0

now = True
later = True
switchValue = True

while True:
        now = button.value
        switchValue = switch.value
        print(str(switchValue))
        if now == False and later == True:
            if switchValue:
                counter += 1
            if not switchValue:
                counter -= 1
            lcd.set_cursor_pos(0,0)
            lcd.print("button presses: ")
            lcd.set_cursor_pos(1,0)
            lcd.print(str(counter))
            lcd.print("  ")
            time.sleep(0.05)
            now = True
            later = button.value
        time.sleep(.05)



