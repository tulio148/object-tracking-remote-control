
from servo_class import Servo
from serial_class import SerialClass

if __name__ == "__main__":
    servo1 =  Servo(32)
    servo1.set_angle(0)

    servo2 =  Servo(33)
    servo2.set_angle(0)

    serial_controller = SerialClass('/dev/ttyACM0')
    serial_controller.connect()

    try:
        while True:
            s = serial_controller.readline()
            if s:
                numbers = s.split(' ')
                if len(numbers) == 2 and numbers[0] and numbers[1]:
                    x = float(numbers[0])
                    y = float(numbers[1])
                    print(x, y)
                    servo1.duty_cycle(x)
                    servo2.duty_cycle(y)
    except KeyboardInterrupt:
        servo1.cleanup()
        servo2.cleanup()
        serial_controller.disconnect()
