import io
import picamera
import time
def PreviewIt():
    camera = picamera.PiCamera()
    try:
        camera.start_preview()
        time.sleep(10)
        camera.stop_preview()
    finally:
        camera.close()
def PreviewTake(dest):
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.start_preview()
        camera.exposure_compensation = 2
        camera.exposure_mode = 'spotlight'
        camera.meter_mode = 'matrix'
        camera.image_effect = 'gpen'
        time.sleep(5)
        camera.capture('/home/pi/Downloads/' + dest + '.jpg')
        camera.stop_preview()
def PiTakeScale(dest, scale):
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.start_preview()
        camera.exposure_compensation = 2
        camera.exposure_mode = 'spotlight'
        camera.meter_mode = 'matrix'
        camera.image_effect = 'gpen'
        time.sleep(5)
        camera.capture('/home/pi/Downloads/' + dest + '.jpg', resize=(1280 / scale, 720 / scale))
        camera.stop_preview()
def RecordMe(dest, lengh):
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_recording('/home/pi/Downloads/' + dest + '.h264')
        camera.wait_recording(leng)
        camera.stop_recording()