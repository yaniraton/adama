from server.Utilities.Motor import Motor
import Constants
import time


class Elevator:

    def __init__(self) -> None:
        self.right_motor = Motor(Constants.ELEVATOR_RIGHT_PORTS)
        self.left_motor = Motor(Constants.ELEVATOR_LEFT_PORTS)


    def move_elevator(self, speed: float, moving_time: float):
        self.right_motor.set(speed)
        self.left_motor.set(speed)

        start_time = time.time()

        while(time.time() - start_time < moving_time):
            time.sleep(0.1)

        self.stop_elevator()

    
    def stop_elevator(self):
        self.right_motor.set(0)
        self.left_motor.set(0)
