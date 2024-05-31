from servo_class import Servo
from serial_class import SerialClass

if __name__ == "__main__":
    # Initialize the first servo on GPIO pin 32 and set its angle to 0
    servo1 = Servo(32)
    servo1.set_angle(0)

    # Initialize the second servo on GPIO pin 33 and set its angle to 0
    servo2 = Servo(33)
    servo2.set_angle(0)

    # Initialize the serial connection on port '/dev/ttyACM0'
    serial_controller = SerialClass('/dev/ttyACM0')
    serial_controller.connect()

    try:
        while True:
            s = serial_controller.readline()
            if s:
                numbers = s.split(' ')
                # Check if both parts are available and valid
                if len(numbers) == 2 and numbers[0] and numbers[1]:
                    x = float(numbers[0])
                    y = float(numbers[1])
                    # Set the duty cycle of the servos to the received values
                    servo1.duty_cycle(x)
                    servo2.duty_cycle(y)
    except KeyboardInterrupt:
        # Cleanup the servos and disconnect the serial connection on interrupt
        servo1.cleanup()
        servo2.cleanup()
        serial_controller.disconnect()
