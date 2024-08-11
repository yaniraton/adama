from server.Utilities.UltrasonicSensor import UltrasonicSensor
from server.Utilities.Camera import Camera
from server.Utilities.Motor import Motor
import Constants
import time

class DriveTrain:
    def __init__(self) -> None:
        self.rightFront = Motor(Constants.RIGHT_FRONT_PORTS)
        self.rightRear = Motor(Constants.RIGHT_REAR_PORTS)
        self.leftFront = Motor(Constants.LEFT_FRONT_PORTS)
        self.leftRear = Motor(Constants.LEFT_REAR_PORTS)
        self.camera = Camera.get_instance()
        self.right_sonic = UltrasonicSensor(0, 0, 0)
        

    def drive(self, leftY: float, leftX: float, rightX: float) -> None:
        """
        This function makes the drivetrain move according to the joystick values.

        Args:
            leftY (float): The y axis value of the left joystick.
            leftX (float): The x axis value of the left joystick.
            rightX (float): The x axis value of the right joystick.
        """
        motorsPowers = self.calcMotorsValues(self, leftY, leftX, rightX)
        
        self.rightFront.set(motorsPowers[0])
        self.rightRear.set(motorsPowers[1])
        self.leftFront.set(motorsPowers[2])
        self.leftRear.set(motorsPowers[3])


    def calcMotorsValues(self, leftY: float, leftX: float, rightX: float) -> tuple:
        """
        This function calculates the values to set to the motors according to the joystick values.

        Args:
            leftY (float): _description_
            leftX (float): _description_
            rightX (float): _description_

        Returns:
            tuple: _description_
        """
        leftX *= Constants.LEFT_X_COFFICIENT

        denominator = max(abs(leftY) + abs(leftX) + abs(rightX), 1)

        rightFrontPower = (leftY - leftX - rightX) / denominator
        rightBackPower = (leftY + leftX - rightX) / denominator
        leftFrontPower = (leftY + leftX + rightX) / denominator
        leftRearPower = (leftY - leftX + rightX) / denominator

        return (rightFrontPower, rightBackPower, leftFrontPower, leftRearPower)


    def drive_until_plant_recognized(self):
        sonic_distance = self.right_sonic.get_distance(0)
        plant_found = True

        # Drives to distance if needed
        if sonic_distance > Constants.DISTANCE_FROM_PLANT:
            plant_found = self.drive_until_distance(Constants.DISTANCE_FROM_PLANT,
                                                     Constants.MAX_SEARCHING_PLANT_TIME)

        if plant_found:
            scanned_data = self.camera.scan_qr()
            return (scanned_data != "", scanned_data)
        else:
            return (False, "")


    def drive_until_distance(self, distance, max_time):
        self.drive(Constants.DRIVE_FORWARD_SPEED, 0, 0)

        start_time = time.time()
        current_time = time.time()
        sonic_distance = self.right_sonic.get_distance(0)
            
        while (sonic_distance > distance) and (current_time - start_time < max_time):
            sonic_distance = self.right_sonic.get_distance(0)
            current_time = time.time()

        self.drive(0, 0, 0)  # Stops driving

        return sonic_distance > distance  # Whether got to the distance or stopped by time