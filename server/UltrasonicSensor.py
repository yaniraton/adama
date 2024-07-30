from gpiozero import DistanceSensor

class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin):
        """ This function initializes the ultrasonic sensor.

        Args:
            trig_pin (int): The GPIO pin number the trigger pin is connected to.
            echo_pin (int): The GPIO pin number the echo pin is connected to.
        """        
        self.sensor = DistanceSensor(echo=echo_pin, trigger=trig_pin)

    def get_distance(self):
        """ This function returns the distance measured by the ultrasonic sensor.

        Returns:
            float: The distance measured by the ultrasonic sensor.
        """
        print(self.sensor.distance)
        return self.sensor.distance