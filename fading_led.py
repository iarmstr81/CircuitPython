import time
import board
import pulseio
from digitalio import DigitalInOut, Direction


pwm_leds = board.D0 # PWM (fading) LEDs are connected on D0
pwm = pulseio.PWMOut(pwm_leds, frequency=1000, duty_cycle=0)


digital_leds = DigitalInOut(board.D2) # digital LEDs connected on D2
digital_leds.direction = Direction.OUTPUT
brightness = 0  # how bright the LED is
fade_amount = 1285  # 2% steping of 2^16
counter = 0  # counter to keep track of cycles

while True:
    pwm.duty_cycle = brightness  # And send to LED as PWM level

    
    brightness = brightness + fade_amount # change the brightness for next time through the loop

    print(brightness)

    # reverse the direction of the fading at the ends of the fade:
    if brightness <= 0:
        fade_amount = -fade_amount
        counter += 1
    elif brightness >= 65535:
        fade_amount = -fade_amount
        counter += 1

    # wait for 15 ms to see the dimming effect
    time.sleep(.015)

    # turns on the other LEDs every four times through the fade by
    # checking the modulo of the counter.
    # the modulo function gives you the remainder of
    # the division of two numbers:
    if counter % 4 == 0:
        digital_leds.value = True
    else:
        digital_leds.value = False