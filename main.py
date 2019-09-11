import time
import board
import adafruit_hcsr04
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D9)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

def constrain(n, minn, maxn):
    return min(max(n, minn), maxn)

while True:
    try:
        print(sonar.distance)
        dot.fill((constrain(int(255-(17*sonar.distance)), 0, 255),constrain(int(255-abs(17*(35-sonar.distance))), 0, 255)\
        ,constrain(int(255-abs(17*(20-sonar.distance))), 0, 255)))
    except RuntimeError:
        print('fail')
        pass
    time.sleep(0.1)