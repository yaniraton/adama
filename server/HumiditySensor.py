from gpiozero import MCP3008

class HumiditySensor:
    def __init__(self, channel: int) -> None:
        """
        This function initializes the humidity sensor.

        Args:
            channel (int): The channel the sensor is connected to on the MCP3008.
        """
        # Setup MCP3008 ADC (assuming it's connected to SPI bus on default pins)
        self.adc = MCP3008(channel=channel)

    def read_soil_moisture(self):
        """
        This function reads the soil moisture level from the sensor.

        Returns:
            float: The soil moisture level as a value between 0 and 1.
        """
        print(self.adc.value)
        return self.adc.value  # Returns a value between 0 and 1

