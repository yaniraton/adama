from server.DB.DataBase import DataBase
from server.Subsystems.Arm import Arm
from server.Subsystems.DriveTrain import DriveTrain
import Controller
import Constants
import threading
from server.Subsystems.Elevator import Elevator
from server.Utilities.HumiditySensor import HumiditySensor
from server.Utilities.AccelSensor import AccelSensor
from DB.Plant import Plant

class Server:

    driveTrain: DriveTrain
    controller: Controller
    arm: Arm
    elevator: Elevator
    humiditySensor: HumiditySensor
    accelSensor: AccelSensor
    data_base: DataBase

    def __init__(self) -> None:
        self.driveTrain = DriveTrain()
        self.arm = Arm()
        elevator = Elevator()
        self.controller = Controller(self.servoMotor.set_servo_angle)
        self.humiditySensor = HumiditySensor.get_instance()
        self.accelSensor = AccelSensor.get_instance()
        self.data_base = DataBase.get_instance()
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

                qr_data = qr_data.split("-")
                self.save_plant_to_db(int(qr_data[0]), int(qr_data[1]), bool(qr_data[2]), soil_moisture)

    def save_plant_to_db(self, column, plant_id, is_tomato, humidity):
        current_plant_data = self.data_base.get_plant_data(plant_id)

        if current_plant_data is not None:
            current_plant_data.set_column(column)
            current_plant_data.set_is_tomato(is_tomato)
            current_plant_data.add_humidity(humidity)
        else:
            current_plant_data = Plant(plant_id, is_tomato, {}, "", column)
            current_plant_data.add_humidity(humidity)

        self.data_base.save_plant(current_plant_data)

