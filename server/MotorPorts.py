class MotorPorts:
    def __init__(self, in1_port, in2_port, ena_port):
        self.in1 = in1_port
        self.in2 = in2_port
        self.en = ena_port

    def getPorts(self):
        return self.in1, self.in2, self.ena
