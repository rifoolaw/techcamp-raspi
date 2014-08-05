print "Importing stuff..."
import time
import picamera
import pcmtks
print "done. Welcome to PiCamera Menu!\n\n"
while True:
    print "Welcome to the PiCamera Menu! With this, you can take photos and more with your PiCamera!"
    print "To make it work, use the commands down here."
    print "PreviewIt: displays what PiCamera sees for 10 seconds."
    print "PreviewTake: displays what PiCamera sees for 5 seconds, and then takes a photo."
    print "PiTakeScale: Preview, take a photo and scale it basing on user preference!"
    print "RecordMe: Want to take a video? This is for you! (videos are in 640 * 480)"
    what = raw_input("")
    if what == "PreviewIt":
        pcmtks.PreviewIt()
    elif what == "PreviewTake":
        destination = raw_input("We'll save the file in the Downloads folder. How you you want to call your file? ")
        pcmtks.PreviewTake(destination)
    elif what == "PiTakeScale":
        destination = raw_input("We'll save the file in the Downloads folder. How you you want to call your file? ")
        scale = raw_input("The image should be scaled by?")
        if scale.type() == float or scale.type() == int:
            pcmtks.PiTakeScale(destination, scale)
        else:
            print "You insterted a string instead of a number on scale!"
    elif what == "RecordMe":
        destination = raw_input("We'll save the file in the Downloads folder. How you you want to call your file? ")
        leng = raw_input("How long should your video be?")
        RecordMe(destination, leng)