import time
import board
import pulseio
from adafruit_motor import servo
import touchio

touch_A5 = touchio.TouchIn(board.A5) #setting up wire in pin
touch_A4 = touchio.TouchIn(board.A4) #setting up wire in pin
touch = touchio.TouchIn 


pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50) #setting up pwm 
my_servo = servo.Servo(pwm)

angle = 0 #amgle starts at zero

while True:
    my_servo.angle = angle
    if touch_A4.value: #if wire 4 gets touched
        print("Touched A4")
        if angle < 180: #if angle is less then 180 add 1 to angle
         angle += 1
        time.sleep(0.05)
    if touch_A5.value: #if wire 5 gets touched 
        print("Touched A5") 
        if angle > 0: #if wire is less then subtract 1
         angle -= 1 
        time.sleep(0.05)



