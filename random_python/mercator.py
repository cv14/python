# mercator.py: Takes three floats l0, phi, and l as command-line arguments and
# prints its projection, i.e., the x and y values separated by a space,
# calculated using x=l-l0 and y=ln((1+sin(phi))/(1-sin(phi)))/2.

import math
import stdio
import sys


l0 = float(sys.argv[1])
phi = math.radians(float(sys.argv[2]))
l = float(sys.argv[3])

x = l-l0
y = 1 + math.sin(phi)
y = y/(1- math.sin(phi))
y = math.log(y)/2
stdio.writeln(str(x) + ' ' + str(y))
