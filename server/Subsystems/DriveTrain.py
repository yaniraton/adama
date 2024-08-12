from server.Utilities.AccelSensor import AccelSensor
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
        self.right_sonic = UltrasonicSensor(Constants.COMMON_SONIC_TRIG, Constants.RIGHT_SONIC_ECHO)
        self.imu = AccelSensor.get_instance()
        

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
        sonic_distance = self.right_sonic.measure_distance()
            
        while (sonic_distance > distance) and (current_time - start_time < max_time):
            sonic_distance = self.right_sonic.measure_distance()
            current_time = time.time()

        self.drive(0, 0, 0)  # Stops driving
        self.lock_drive_train()

        return sonic_distance > distance  # Whether got to the distance or stopped by time
    

    def lock_drive_train(self):
        """
        This function locks the drivetrain motors.
        """        
        self.rightFront.lock()
        self.rightRear.lock()
        self.leftFront.lock()
        self.leftRear.lock()


    def rotate_to_angle(self, target_angle: float, tolerance: float = 1.0, max_time: float = 5.0) -> None:
        """
        Rotates the robot to the specified angle using the IMU sensor.

        Args:
            target_angle (float): The desired angle to rotate to, in degrees.
            tolerance (float): The acceptable range of error for the target angle.
            max_time (float): The maximum time allowed to complete the rotation, in seconds.
        """
        start_time = time.time()
        current_time = start_time
        
        while current_time - start_time < max_time:
            # Read current gyroscope data (assuming Z-axis is the yaw angle)
            gyro_x, gyro_y, current_angle = self.imu.read_gyroscope()
            
            # Calculate the error
            error = target_angle - current_angle
            
            # Check if within tolerance
            if abs(error) <= tolerance:
                break
            
            # Determine the direction and speed to rotate
            rotation_speed = Constants.ROTATION_SPEED * (error / abs(error))  # Rotate left or right based on the sign of the error
            
            # Apply the rotation to the motors
            self.drive(0, 0, rotation_speed)
            
            # Update the current time
            current_time = time.time()
        
        # Stop the robot after reaching the target angle
        self.drive(0, 0, 0)
        self.lock_drive_train()
