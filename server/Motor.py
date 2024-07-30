from gpiozero import OutputDevice, PWMOutputDevice
from server.MotorPorts import MotorPorts


class Motor:

    def __init__(self, ports: MotorPorts) -> None:
        self.in1 = OutputDevice(ports.in1)
        self.in2 = OutputDevice(ports.in2)
        self.en = PWMOutputDevice(ports.en) 


    def set(self, speed: float) -> None:
        """
        This function sets a given speed to this motor.

        Args:
            speed (float): A floating-point value between -1 and 1, which represents the precentage speed to set to the motor.
        """            
        if speed > 0:
            self.in1.on()
            self.in2.off()
        elif speed < 0:
           self.in1.on()
           self.in2.off()
           
        self.en.value = speed


