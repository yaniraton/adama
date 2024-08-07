
from server.Utilities.HumiditySensor import HumiditySensor
from server.Utilities.ServoMotor import ServoMotor
import Constants
import time

class Arm:

    def __init__(self, servo_pin: int, humidity_sensor_pin: int) -> None:
        self.servo = ServoMotor(servo_pin)
        self.humidity_sensor = HumiditySensor(humidity_sensor_pin)


    def open_arm(self) -> None:
        self.servo.set_servo_angle(Constants.OPENED_ARM_ANGLE)


    def close_arm(self) -> None:
        self.servo.set_servo_angle(Constants.CLOSED_ARM_ANGLE)


    def measure_soil_moisture_operation(self):
        self.open_arm()
        time.sleep(0.5)

        soil_moisture = None
        while soil_moisture is None:
            soil_moisture = self.humidity_sensor.read_soil_moisture()

        time.sleep(0.5)
        self.close_arm()

        return soil_moisture
