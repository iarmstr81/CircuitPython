import pulseio
import time
class RGB:
    kind="colors"
    def __init__(self, r, g, b):
        print("you just made an object!")
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)

    def change_name(self, newName):
        self.name = newName

    def change_pins(self, r, g, b):
        self.r = r

    def red(self):
        self.pwm_r.duty_cycle = 0 #red led on
        self.pwm_g.duty_cycle = 2**16-1 #green off
        self.pwm_b.duty_cycle = 2**16-1 #blue off

    def blue(self):
        self.pwm_r.duty_cycle = 2**16-1 #red off
        self.pwm_g.duty_cycle = 2**16-1 #green off
        self.pwm_b.duty_cycle = 0 #blue on

    def magenta(self):
        self.pwm_r.duty_cycle = 0 #red on
        self.pwm_g.duty_cycle = 2**16-1 #green off
        self.pwm_b.duty_cycle = 0 #blue on

    def cyan(self):
        self.pwm_r.duty_cycle = 2**16-1 #red off
        self.pwm_g.duty_cycle = 0 #green on
        self.pwm_b.duty_cycle = 0 #blue on

    def green(self):
        self.pwm_r.duty_cycle = 2**16-1 #red off
        self.pwm_g.duty_cycle = 0 #green on
        self.pwm_b.duty_cycle = 2**16-1 #blue off

    def yellow(self):
        self.pwm_r.duty_cycle = 0 #red on
        self.pwm_g.duty_cycle = 0 #green on
        self.pwm_b.duty_cycle = 2**16-1 #blue off

    def rainbow(self):
        #go through all colors
        self.pwm_r.duty_cycle = 0 #red starts on
        self.pwm_g.duty_cycle = 2**16-1 #green starts off
        self.pwm_b.duty_cycle = 2**16-1 #blue starts off
        for val in range(0,2**16,64): #in a range of 0 - 2**16 by 64 increments do below
            #red
            self.pwm_r.duty_cycle = val #red is turning off slowly
            self.pwm_g.duty_cycle = 2**16-1-val #green is turning on slowly
            self.pwm_b.duty_cycle = 2**16-1 #blue is off
            time.sleep(.01)
        for val in range(0,2**16,64):
            #green
            self.pwm_r.duty_cycle = 2**16-1 #red is now off
            self.pwm_g.duty_cycle = val #green is turning off slowly
            self.pwm_b.duty_cycle = 2**16-1-val #blue is turning on slowly
            time.sleep(.01)
        for val in range(0,2**16,64):
            #blue
            self.pwm_r.duty_cycle = 2**16-1-val #red is turning back on
            self.pwm_g.duty_cycle = 2**16-1 #green is off
            self.pwm_b.duty_cycle = val #blue is slowly turning off
            time.sleep(.01)