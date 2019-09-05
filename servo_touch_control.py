import time
import board
import pulseio
from adafruit_motor import servo
import touchio

touch_A5 = touchio.TouchIn(board.A5)
touch_A4 = touchio.TouchIn(board.A4)
touch = touchio.TouchIn


pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

angle = 0

while True:
    my_servo.angle = angle
    if touch_A4.value:
        print("Touched A4")
        if angle < 180:
         angle += 1
        time.sleep(0.05)
    if touch_A5.value:
        print("Touched A5")
        if angle > 0:
         angle -= 1
        time.sleep(0.05)



