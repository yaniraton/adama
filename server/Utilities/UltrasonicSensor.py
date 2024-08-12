from gpiozero import DistanceSensor

class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin):
        """Initializes the UltrasonicSensor object

        Args:
            trig_pin (int): The pin number of the TRIG pin of the ultrasonic sensor
            echo_pin (int): The pin number of the ECHO pin of the ultrasonic sensor
        """        
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin

    def choose_echo_pin(self, echo_pin):
        """Chooses the ECHO pin of the ultrasonic sensor

        Args:
            echo_pin (int): The pin number of the ECHO pin of the ultrasonic sensor
        """        
        self.echo_pin = echo_pin

    def measure_distance(self,eecho_pin=-1):
        """Measures the distance between the ultrasonic sensor and the object in front of it

        Returns:
            float: The distance between the ultrasonic sensor and the object in front of it
        """ 
        if eecho_pin == -1:
            eecho_pin = self.echo_pin
        sensor = DistanceSensor(echo=eecho_pin, trigger=self.trig_pin)
        distance = sensor.distance
        del sensor  # Delete the sensor object to release the TRIG pin
        return distance