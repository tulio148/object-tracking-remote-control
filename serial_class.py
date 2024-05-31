import serial

class SerialClass:
    """
    A class to manage serial communication.

    Attributes:
    ----------
    port : str
        The port to which the serial device is connected.
    baudrate : int, optional
        The baud rate for the serial communication (default is 9600).
    timeout : float, optional
        The timeout value for the serial communication (default is 1 second).

    Methods:
    -------
    connect():
        Establishes the serial connection.
    readline():
        Reads a line from the serial port.
    disconnect():
        Closes the serial connection.
    """

    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None  # Initialize serial connection as None

    def connect(self):
        self.serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)

    def readline(self):
        if self.serial:
            return self.serial.readline().decode('utf-8').strip()

    def disconnect(self):
        if self.serial:
            self.serial.close()
