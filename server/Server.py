from server.Subsystems.Arm import Arm
from server.Subsystems.DriveTrain import DriveTrain
import Controller
import Constants
import threading
from server.Subsystems.Elevator import Elevator
from server.Utilities.HumiditySensor import HumiditySensor
from server.Utilities.AccelSensor import AccelSensor
from typing import List
from server.Utilities.UltrasonicSensor import UltrasonicSensor

class Server:

    driveTrain: DriveTrain
    controller: Controller
    arm: Arm
    elevator: Elevator
    ultraSonicSensors: List[UltrasonicSensor] = []
    humiditySensor: HumiditySensor
    accelSensor: AccelSensor

    def __init__(self) -> None:
        self.driveTrain = DriveTrain()
        self.arm = Arm()
        elevator = Elevator()
        self.controller = Controller(self.servoMotor.set_servo_angle)
        for trig, echo in Constants.SONIC:
            self.ultraSonicSensors.append(UltrasonicSensor(trig, echo))
        self.humiditySensor = HumiditySensor.get_instance()
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
        self.controller.add_to_cross_pressed(self.arm.open_arm)
        self.controller.add_to_circle_pressed(self.arm.close_arm)
        self.controller.add_to_triangle_pressed(self.humiditySensor.read_soil_moisture)
        self.controller.add_to_square_pressed(self.accelSensor.printData)
        
        self.controller.add_to_dpad_up(self.ultraSonicSensors[0].get_distance)
        self.controller.add_to_dpad_right(self.ultraSonicSensors[1].get_distance)
        self.controller.add_to_dpad_left(self.ultraSonicSensors[2].get_distance)
        self.controller.add_to_dpad_down(self.ultraSonicSensors[3].get_distance)

    
    def auto_run_robot(self):
        found, qr_data = True, ""

        while found:
            found, qr_data = self.driveTrain.drive_until_plant_recognized()

            if found:
                elevator_thread = threading.Thread(target=self.elevator.capture_plant, args=("video_file_name.mp4"))
                elevator_thread.start()
                elevator_thread.join()

                soil_moisture = self.arm.measure_soil_moisture_operation()

                # Write to DB