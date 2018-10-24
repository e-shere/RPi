import picamera
import picamera.array
import numpy as np

class MotionDetector(picamera.array.PiMotionAnalysis):
    def analyse(self,a):
        a = np.sqrt(np.square(a['x'].astype(np.float)) + np.square(a['y'].astype(np.float))).clip(0,255).astype(np.uint8)

        if (a>60).sum() >3:
            print("Motion detected")

with picamera.PiCamera() as camera:
    counter=1
    while True:
        location = '/root/Videos/'+str(counter)+'.h264'
        camera.resolution = (1640,1232)
        camera.rotation = 180
        camera.framerate = 30
        camera.start_recording(location,format="h264",motion_output=MotionDetector(camera))
        camera.wait_recording(30)
        camera.stop_recording()
        counter+=1
        print(counter)
