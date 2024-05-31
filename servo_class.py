import RPi.GPIO as GPIO
from time import sleep

class Servo:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50) 
        self.pwm.start(0)
    def set_angle(self, angle):
        duty = angle 
        # sleep(1)  
        
    def duty_cycle(self, angle):
        self.pwm.ChangeDutyCycle(angle)
        sleep(0.1)

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()
        
