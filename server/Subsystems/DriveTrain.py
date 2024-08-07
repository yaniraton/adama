from server.Utilities.Motor import Motor
import Constants

class DriveTrain:
    def __init__(self, ports : tuple) -> None:
        self.rightFront = Motor(ports[0])
        self.rightRear = Motor(ports[1])
        self.leftFront = Motor(ports[2])
        self.leftRear = Motor(ports[3])
        

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
