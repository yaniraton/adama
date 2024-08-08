import cv2 as cv
import time

class Camera:
    def __init__(self, camera_port: int, fps: float, resolution: tuple) -> None:
        self.camera_port = camera_port
        self.fps = fps
        self.resolution = resolution
        self.fourcc = cv.VideoWriter_fourcc(*'MJPG')

    
    def capture_video(self, file_name, capture_time):
        capture = cv.VideoCapture(self.camera_port)
        out_file = cv.VideoWriter(file_name, self.fourcc, self.fps, self.resolution)

        start_time = time.time()

        while (capture.isOpened()) and (time.time() - start_time < capture_time):
            ret, frame = capture.read()

            if not ret:
                print("Can't receive frame")
                start_time = 0  # Breaks the loop
        
            # write the flipped frame
            out_file.write(frame)
            cv.imshow('frame', frame)

        # Release everything if job is finished
        capture.release()
        out_file.release()
        cv.destroyAllWindows()
