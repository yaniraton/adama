from pydualsense import pydualsense
import Constants

class Controller:
    def __init__(self,servoFunc):
        self.ds = pydualsense()
        self.leftY = 0.0
        self.leftX = 0.0
        self.rightX = 0.0
        self.servoFunc = servoFunc
    
    
    def set_left_values(self, leftX : float, leftY: float):
        """
        This function sets the values of the left joystick, between -1 and 1.

        Args:
            leftX (float): The x axis value of the left joystick, between -128 and 128.
            leftY (float): The y axis value of the left joystick, between -128 and 128.
        """
        self.leftY = leftY / Constants.HALF_BYTE
        self.leftX = leftX / Constants.HALF_BYTE
    
    
    def set_right_values(self, rightX: float, rightY: float):
        """
        This function sets the values of the right joystick, between -1 and 1.

        Args:
            rightX (float): The x axis value of the right joystick, between -128 and 128.
            rightY (float): The y axis value of the right joystick, between -128 and 128.
        """        
        self.rightX = rightX / Constants.HALF_BYTE
    
    
    def connect(self) -> bool:
        """
        This function connects the joystick to the program, and sets the event handlers to listen to the joysticks changes.

        Returns:
            bool: Returns whether or not the connection was succsessful.
        """        
        try:
            self.ds.init()
        except Exception as e:  # Catch any Exception
            if str(e) == "No device detected":  # Check for the exact message
                print("Error: No contoler was found.")
            else:
                print("An unexpected error occurred:", e)
            return False
        self.ds.left_joystick_changed += self.set_left_values
        self.ds.right_joystick_changed += self.set_right_values
        return True

    
    def get_joisticks_values(self) -> tuple:
        """
        This function gets the current state of the joysticks.

        Returns:
            tuple: A tuple which contains the left joystick Y, left joystick X and right joystick X in that exact order.
            All of them are values between -1 and 1.
        """         
        return (self.leftY, self.leftX, self.rightX)
    
    def add_to_cross_pressed(self, func, angle):
        self.ds.cross_pressed += lambda: func(angle)

    def add_to_circle_pressed(self, func, angle):
        self.ds.circle_pressed += lambda: func(angle)
    
    def add_to_triangle_pressed(self, func):
        self.ds.triangle_pressed += func

    def add_to_square_pressed(self, func):
        self.ds.square_pressed += func
    
    def add_to_dpad_up(self, func):
        self.ds.dpad_up += func

    def add_to_dpad_down(self, func):
        self.ds.dpad_down += func

    def add_to_dpad_left(self, func):
        self.ds.dpad_left += func
    
    def add_to_dpad_right(self, func):
        self.ds.dpad_right += func
