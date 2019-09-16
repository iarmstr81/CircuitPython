import time
import board
import adafruit_hcsr04
import math
import simpleio
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D11)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

r = 0
b = 0
g = 0
print("is this even working???")
while True:
    try:
        if sonar.distance <= 20:
            r = simpleio.map_range(sonar.distance, 0, 20, 255, 0)
            b = simpleio.map_range(sonar.distance, 5, 20, 0, 255)
            g = simpleio.map_range(sonar.distance, 20, 35, 0, 255)
        else:
            r = simpleio.map_range(sonar.distance, 0, 20, 255, 0)
            b = simpleio.map_range(sonar.distance, 20, 35, 255, 0)
            g = simpleio.map_range(sonar.distance, 20, 35, 0, 255)
        time.sleep(0.1)
        dot.fill((int(r),int(g),int(b)))

            #print((sonar.distance,))
            #mapped_value = simpleio.map_range(sonar.distance, 0, 100, 0, 10)
    except RuntimeError:
        time.sleep(0.1)