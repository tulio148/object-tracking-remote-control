# Servo Control Project

This project demonstrates how to control two servo motors using a Raspberry Pi and read angles from a serial input to adjust the servos.

## Project Structure

project/
│
├── servo_class.py
### Contains the Servo class for controlling a servo motor
├── serial_class.py 
### Contains the SerialClass for handling serial communication
├── main.py 
### Main script to run the project
└── README.md
### Project documentation


## Requirements

- Raspberry Pi
- Two servo motors
- Serial input device (e.g., Arduino, USB-to-serial adapter)
- Python 3
- `RPi.GPIO` library for GPIO control
- `pyserial` library for serial communication

## Installation

1. Clone this repository to your Raspberry Pi.
2. Install the required libraries using pip:
    ```bash
    pip install RPi.GPIO pyserial
    ```

## Usage

1. Connect the servo motors to GPIO pins 32 and 33 on the Raspberry Pi.
2. Connect the serial input device to the Raspberry Pi.
3. Update the serial port in the `main.py` file to match your device (e.g., `/dev/ttyACM0`).

### Running the Project

1. Ensure the servo motors and serial device are properly connected.
2. Run the main script:
    ```bash
    python main.py
    ```
3. The script will read angles from the serial input and adjust the servos accordingly.

### License
This project is licensed under the MIT License.

    def cleanup(self):
