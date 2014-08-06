print "Initializing program."
import makeitspin
import time
print "All the things were imported successufuly.\n\n\n"
while True:
    print "=====================================\nMake it spin!\n====================================="
    print "Wave Drive: wv"
    print "Full Step Drive: fs"
    print "Half Step Drive: hs"
    print "Type the abbreviation to start and see!\nYou can also type \"help\" to view more info about the various drives!"
    what = raw_input("Command: ")
    if what == "wv" or what == "fs" or what = "hs":
        times = raw_input("times: ")
        times = int(float(times))
        print "We'll start in 2 seconds. Watch your Stepper Motor!"
        makeitspin.rotate(times, what)
        print "Finished!"
    elif what = "help":
        print "All of this is taken from Wikipedia.\nWave or Full Step drive: In this drive method only a single phase is activated at a time. It has the same number of steps as the full step drive, but the motor will have significantly less than rated torque. It is rarely used. The animated figure shown above is a wave drive motor. In the animation, rotor has 25 teeth and it takes 4 steps to rotate by one teeth position. So there will be 25*4 = 100 steps per full rotation and each step will be 360/100 = 3.6 degrees.\nFull step drive: This is the usual method for full step driving the motor. Two phases are always on so the motor will provide its maximum rated torque. As soon as one phase is turned off, another one is turned on. Wave drive and single phase full step are both one and the same, with same number of steps but difference in torque.\nHalf step drive: When half stepping, the drive alternates between two phases on and a single phase on. This increases the angular resolution. The motor also has less torque (approx 70%) at the full step position (where only a single phase is on). This may be mitigated by increasing the current in the active winding to compensate. The advantage of half stepping is that the drive electronics need not change to support it. In animated figure shown above, if we change it to half stepping, then it will take 8 steps to rotate by 1 teeth position. So there will be 25*8 = 200 steps per full rotation and each step will be 360/200 = 1.8 degrees. Its angle per step is half of the full step."
    else:
        print "That command isn't associated with anything."