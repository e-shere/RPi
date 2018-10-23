from picamera import PiCamera
from picamera.array import PiRGBArray
from PIL import Image

camera = PiCamera()
camera.resolution = (1640,1232)
camera.rotation = 180
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(1640,1232))

for f in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
    im = Image.fromarray(f.array)
    im.save('1.jpg')
    break
