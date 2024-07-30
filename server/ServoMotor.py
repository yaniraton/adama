from gpiozero import Servo
import time


class ServoMotor:
    def __init__(self, pin: int) -> None:
        """
        This function initializes the servo motor.

        Args:
            pin (int): The GPIO pin number the servo motor is connected to.
        """
        # Servo Setup
        self.servo = Servo(pin)

    def set_servo_angle(self, angle: int) -> None:
        """
        This function sets the angle of the servo motor.

        Args:
            angle (int): The angle to set the servo to (0-180).
        """
        # Convert angle to servo value (-1 to 1)
        servo_value = (angle - 90) / 90

        # Set the servo position
        self.servo.value = servo_value