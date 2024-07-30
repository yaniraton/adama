class MotorPorts:
    def __init__(self, in1_port, in2_port, en_port):
        """
        Constructor function of the MotorPorts class.

        Args:
            in1_port (int): the in1 port - OutputDevice(digital)
            in2_port (int): the in2 port - OutputDevice(digital)
            en_port (int): the en port - PWMOutputDevice(analog)
        """
        self.in1 = in1_port
        self.in2 = in2_port
        self.en = en_port

    def getPorts(self):
        """
        This function returns the ports of a motor.

        Returns:
            tuple(int): the motor ports.
        """
        return self.in1, self.in2, self.en
