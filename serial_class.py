import serial

class SerialClass:
    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None

    def connect(self):
        self.serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)

    def readline(self):
        if self.serial:
            return self.serial.readline().decode('utf-8').strip()

    def disconnect(self):
        if self.serial:
            self.serial.close()
