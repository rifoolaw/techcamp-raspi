print "Importing stuff..."
import pibrella
import time
import pibrellaporcupine
print "done. Welcome to Pibrella Porcupine.\n\n"
while True:
    print "Welcome to Pibrella Porcupine! The sequences and \"Games\" that we have is the following:"
    print "Sequences: HelloPorcupine "
    print "Games:     "
    print "\n\nTo start one of them, just type its name and digit enter!\nYou can quit Pibrella Porcupine anytime by pressing CTRL + C"
    what = raw_input("")
    if what == "HelloPorcupine":
        pibrellaporcupine.HelloPorcupine()
    