import smbus2
import time

class AccelSensor:
    def __init__(self, bus=1, address=0x69):
        self.bus = smbus2.SMBus(bus)
        self.address = address
        
        # Registers (assuming default values)
        self.ACCEL_XOUT_H = 0x3B
        self.ACCEL_XOUT_L = 0x3C
        self.GYRO_XOUT_H = 0x43
        self.GYRO_XOUT_L = 0x44
        self.MAG_XOUT_L = 0x0C  # Example register address, check datasheet for exact values
    
    def read_word(self, register):
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)
        value = (high << 8) + low
        return value
    
    def read_accelerometer(self):
        x = self.read_word(self.ACCEL_XOUT_H)
        y = self.read_word(self.ACCEL_XOUT_H + 2)
        z = self.read_word(self.ACCEL_XOUT_H + 4)
        return x, y, z
    
    def read_gyroscope(self):
        x = self.read_word(self.GYRO_XOUT_H)
        y = self.read_word(self.GYRO_XOUT_H + 2)
        z = self.read_word(self.GYRO_XOUT_H + 4)
        return x, y, z
    
    def read_magnetometer(self):
        x = self.read_word(self.MAG_XOUT_L)
        y = self.read_word(self.MAG_XOUT_L + 2)
        z = self.read_word(self.MAG_XOUT_L + 4)
        return x, y, z
    
    def printData(self):
        accel_x, accel_y, accel_z = self.read_accelerometer()
        gyro_x, gyro_y, gyro_z = self.read_gyroscope()
        mag_x, mag_y, mag_z = self.read_magnetometer()
        
        print(f"Accelerometer: X={accel_x}, Y={accel_y}, Z={accel_z}")
        print(f"Gyroscope: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")
        print(f"Magnetometer: X={mag_x}, Y={mag_y}, Z={mag_z}")