# import stuff
import pibrella
# put sequences
wave_sequence = [1,0,0,0,
		 0,1,0,0,
		 0,0,1,0,
		 0,0,0,1]
full_step_sequence = [1,0,0,1,
                      1,1,0,0,
                      0,1,1,0,
                      0,0,1,1]
half_step_drive = [1,0,0,1,
                   1,0,0,0,
                   1,1,0,0,
                   0,1,0,0,
                   0,1,1,0,
                   0,0,1,0,
                   0,0,1,1,
                   0,0,0,1]
# function
def rotate(times, method):
    # check the method and put stuff into variable usemeth
    if method == "wv":
        global wave_sequence
        usemeth = wave_sequence
    elif method == "fs":
        global full_step_sequence
        usemeth = full_step_sequence
    elif method == "hs":
        global half_step_drive
        usemeth = half_step_drive
    # starts the loop.
    usecount = 1
    while times != 0:
        for binum in usemeth:
            if usecount == 1:
                pibrella.output.e.write(binum)
                usecount += 1
            elif usecount == 2:
                pibrella.output.f.write(binum)
                usecount += 1
            elif usecount == 3:
                pibrella.output.g.write(binum)
                usecount += 1
            elif usecount == 4:
                pibrella.output.h.write(binum)
                usecount = 1
        times = times - 1
    pibrella.output.write(0)