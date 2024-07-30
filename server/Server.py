import DriveTrain
import ServoMotor
import Controller
import Constants
import threading
import HumiditySensor
import AccelSensor
from typing import List
from UltrasonicSensor import UltrasonicSensor

class Server:

    driveTrain: DriveTrain
    controller: Controller
    servoMotor: ServoMotor
    ultraSonicSensors: List[UltrasonicSensor] = []
    humiditySensor: HumiditySensor
    accelSensor: AccelSensor

    def __init__(self) -> None:
        ports = (Constants.RIGHT_FRONT_PORTS, Constants.RIGHT_REAR_PORTS, Constants.LEFT_FRONT_PORTS, Constants.LEFT_REAR_PORTS)
        self.driveTrain = DriveTrain(ports)
        self.servoMotor = ServoMotor(Constants.SERVO_PORT)
        self.controller = Controller(self.servoMotor.set_servo_angle)
        for trig, echo in Constants.SONIC:
            self.ultraSonicSensors.append(UltrasonicSensor(trig, echo))
        self.humiditySensor = HumiditySensor(Constants.HUMIDITY_SENSOR_PORT)
        self.accelSensor = AccelSensor
        self.configure_buttons()

        # TODO: add the comunicator object when it is ready

    def run(self) -> None:
        # TODO: create a communicator thread
        while(not self.controller.init):
            input()
            
        self.startDrive()
    

    def startDrive(self):
        self.driveTrain.drive(self.controller.get_joisticks_values())
        thread = threading.Timer(0.02, self.startDrive)

        thread.start()
        thread.join()


    def configure_buttons(self):
        self.controller.add_to_cross_pressed(self.servoMotor.set_servo_angle, 0)
        self.controller.add_to_circle_pressed(self.servoMotor.set_servo_angle, 180)
        self.controller.add_to_triangle_pressed(self.humiditySensor.read_soil_moisture)
        self.controller.add_to_square_pressed(self.accelSensor.printData)
        
        self.controller.add_to_dpad_up(self.ultraSonicSensors[0].get_distance)
        self.controller.add_to_dpad_right(self.ultraSonicSensors[1].get_distance)
        self.controller.add_to_dpad_left(self.ultraSonicSensors[2].get_distance)
        self.controller.add_to_dpad_down(self.ultraSonicSensors[3].get_distance)