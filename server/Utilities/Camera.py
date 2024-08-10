import cv2 as cv
import time
from qreader import QReader

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

            else:
                # write the flipped frame
                out_file.write(frame)
                cv.imshow('frame', frame)

        # Release everything if job is finished
        capture.release()
        out_file.release()
        cv.destroyAllWindows()


    def scan_qr(self):
        capture = cv.VideoCapture(self.camera_port)
        ret, frame = capture.read()

        if ret:
            # Releases the camera
            capture.release()
            cv.destroyAllWindows()

            # Creates a QReader instance
            qreader = QReader()

            # Gets the image that contains the QR code
            image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

            # Uses the detect_and_decode function to get the decoded QR data
            decoded_text = qreader.detect_and_decode(image=image)

            if len(decoded_text) > 0:
                return decoded_text[0]
            else:
                return None

        else:
            print("Can't receive frame")
            return None
