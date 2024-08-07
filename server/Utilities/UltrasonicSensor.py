import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
import time

class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin, mux_pins):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.mux_pins = mux_pins
        self.sensor = DistanceSensor(echo=echo_pin, trigger=trig_pin)

    def get_distance(self, channel):
        # Set mux pins based on channel
        GPIO.output(self.mux_pins[0], (channel & 1) == 1)
        GPIO.output(self.mux_pins[1], (channel & 2) == 2)
        GPIO.output(self.mux_pins[2], (channel & 4) == 4)

        # Allow some time for mux to settle
        time.sleep(0.001)

        # Trigger sensor and get distance
        self.sensor.trigger()
        distance = self.sensor.distance
        time.sleep(0.1)  # Avoid overwhelming the sensor

        return distance