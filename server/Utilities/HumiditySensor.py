import RPi.GPIO as GPIO
import time

class HumiditySensor:
    def __init__(self, pin: int) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)

        self.pin = pin


    def measure_pwm(self):
        # Measure the length of high and low pulses
        start_time = time.time()
    
        while GPIO.input(self.pin) == GPIO.LOW:
            if time.time() - start_time > 1:
                return None  # Timeout
        
        start = time.time()

        while GPIO.input(self.pin) == GPIO.HIGH:
            if time.time() - start > 1:
                return None  # Timeout
        
        high_time = time.time() - start
        
        start = time.time()

        while GPIO.input(self.pin) == GPIO.LOW:
            if time.time() - start > 1:
                return None  # Timeout
        
        low_time = time.time() - start
        
        return high_time, low_time


    def read_soil_moisture(self):
        try:
            pulse_times = self.measure_pwm(self.pin)
                
            if pulse_times is None:
                print("Timeout occurred while reading PWM signal.")
                return None
            else:
                high_time, low_time = pulse_times
                total_time = high_time + low_time
                duty_cycle = (high_time / total_time) * 100  # Calculates percentage

        except KeyboardInterrupt:
            pass

        finally:
            GPIO.cleanup()

        return duty_cycle
