import server.Utilities.MotorPorts as MotorPorts

LEFT_X_COFFICIENT = 1.1
HALF_BYTE = 128

# motor ports define
RIGHT_FRONT_PORTS = MotorPorts(0, 0, 0)
RIGHT_REAR_PORTS = MotorPorts(0, 0, 0)
LEFT_FRONT_PORTS = MotorPorts(0, 0, 0)
LEFT_REAR_PORTS = MotorPorts(0, 0, 0)
SERVO_PORT = 0

# 4 ultrasonic sensors
FRONT_SONIC_TRIG = 17
FRONT_SONIC_ECHO = 18

RIGHT_SONIC_TRIG = 22
RIGHT_SONIC_ECHO = 23

LEFT_SONIC_TRIG = 24
LEFT_SONIC_ECHO = 25

REAR_SONIC_TRIG = 27
REAR_SONIC_ECHO = 4

SONIC =[(FRONT_SONIC_TRIG, FRONT_SONIC_ECHO), (RIGHT_SONIC_TRIG, RIGHT_SONIC_ECHO), (LEFT_SONIC_TRIG, LEFT_SONIC_ECHO), (REAR_SONIC_TRIG, REAR_SONIC_ECHO)]

HUMIDITY_SENSOR_PORT = 0

# Arm
OPENED_ARM_ANGLE = 90
CLOSED_ARM_ANGLE = 0

#Elevator
ELEVATOR_RIGHT_PORTS = MotorPorts(0, 0, 0)
ELEVATOR_LEFT_PORTS = MotorPorts(0, 0, 0)
ELEVATOR_MOVING_SPEED = 0.3
ELEVATOR_MOVING_TIME = 2  # In seconds
