import RPi.GPIO as GPIO
from time import sleep

class Servo:
    """
    A class to control a servo motor using Raspberry Pi GPIO.

    Attributes:
    ----------
    pin : int
        The GPIO pin number to which the servo is connected.

    Methods:
    -------
    set_angle(angle):
        Sets the servo to the specified angle.
    duty_cycle(angle):
        Changes the PWM duty cycle to control the servo angle.
    cleanup():
        Stops the PWM and cleans up the GPIO settings.
    """

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(self.pin, GPIO.OUT) 
        self.pwm = GPIO.PWM(self.pin, 50) 
        self.pwm.start(0)  

    def set_angle(self, angle):
        duty = angle  
        sleep(0.1)
        
    def duty_cycle(self, angle):
        self.pwm.ChangeDutyCycle(angle) 
        sleep(0.1)  

    def cleanup(self):
        self.pwm.stop()  
        GPIO.cleanup()  
