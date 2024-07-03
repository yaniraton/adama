from gpiozero import OutputDevice, PWMOutputDevice

class Motor:

    def __init__(self, in1_port, in2_port, ena_port):
        self.in1 = OutputDevice(in1_port)
        self.in2 = OutputDevice(in2_port)
        self.en = PWMOutputDevice(ena_port) 


    def set(self, speed: float):
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


