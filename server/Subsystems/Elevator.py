import threading
from server.Utilities.Camera import Camera
from server.Utilities.Motor import Motor
import Constants
import time


class Elevator:

    def __init__(self) -> None:
        self.right_motor = Motor(Constants.ELEVATOR_RIGHT_PORTS)
        self.left_motor = Motor(Constants.ELEVATOR_LEFT_PORTS)
        self.camera = Camera(Constants.CAMERA_PORT, Constants.CAMERA_FPS, Constants.CAMERA_RESOLUTION)


    def move_elevator(self, speed: float, moving_time: float):
        self.right_motor.set(speed)
        self.left_motor.set(speed)

        start_time = time.time()

        while(time.time() - start_time < moving_time):
            time.sleep(0.1)

        self.stop_elevator()


    def open_elevator(self, video_file_name):
        camera_thread = threading.Thread(target=self.camera.capture_video, args=(video_file_name, Constants.ELEVATOR_OPEN_TIME))
        camera_thread.start()
        camera_thread.join()

        self.move_elevator(Constants.ELEVATOR_OPEN_SPEED, Constants.ELEVATOR_OPEN_TIME)


    def close_elevator(self):
        self.move_elevator(Constants.ELEVATOR_CLOSE_SPEED, Constants.ELEVATOR_CLOSE_TIME)
    

    def stop_elevator(self):
        self.right_motor.set(0)
        self.left_motor.set(0)
