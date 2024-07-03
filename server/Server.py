import DriveTrain
import Controller
import Constants
import threading

class Server:

    driveTrain: DriveTrain
    controller: Controller

    def __init__(self) -> None:
        ports = (Constants.RIGHT_FRONT_PORTS, Constants.RIGHT_REAR_PORTS, Constants.LEFT_FRONT_PORTS, Constants.LEFT_REAR_PORTS)
        self.driveTrain = DriveTrain(ports)
        self.controller = Controller()
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
