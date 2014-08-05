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
        camera.capture('/pi/home/Downloads/' + destination + '.jpg')
        camera.stop_preview()
def PiTakeScale(dest, scale):
    with picamera.PiCamera() as camera:
        camera.resolution = (1280 / scale, 720 / scale)
        camera.start_preview()
        camera.exposure_compensation = 2
        camera.exposure_mode = 'spotlight'
        camera.meter_mode = 'matrix'
        camera.image_effect = 'gpen'
        time.sleep(5)
        camera.capture('/pi/home/Downloads/' + destination + '.jpg')
        camera.stop_preview()