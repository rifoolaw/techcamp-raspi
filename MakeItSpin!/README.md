# Make it spin!
Make the stepper motor spin with your Raspberry Pi! To start it fast, just execute in your python shell `makeitspin_exec.py`. You will be guided on how to execute the function. Otherwise, if you want to include this into your python project, just add makeitspin.py in your folder and then in your file do `import makeitspin`. Or also `from makeitspin import rotate`.

# Using the function
```python
import makeitspin
makeitspin.rotate(TIMES_TO_REPEAT, METHOD)
```

The method can be [`"wv"`](http://en.wikipedia.org/wiki/Stepper_motor#Wave_drive_or_Full_step_drive_.28one_phase_on.29), [`"fs"`](http://en.wikipedia.org/wiki/Stepper_motor#Full_step_drive_.28two_phases_on.29) or [`"hs"`](http://en.wikipedia.org/wiki/Stepper_motor#Half_stepping).

The times to repeat it's the number of times the loop needs to be repeated. If it's only one time, the disc just moves for like 0.01 millimeters. But when it gets at 100 and more, you can clearly see that moving!

## Examples
```python
import makeitspin
makeitspin.rotate(1000, "fs")
```
or:

```python
from makeitspin import rotate
rotate(1000, "fs")
```