# root.py: takes a float c and an integer k as command-line arguments and
# writes the kth root of c to 5 decimal places of accuracy.

import stdio
import sys
import math

# Get c from command line, as a float.
c = float(sys.argv[1])

# Get k from command line, as an int.
k = int(sys.argv[2])

# Define epsilon to be 0.00001 (for 5 decimal places of accuracy).
epsilon = 0.00001

# Define a variable t (kth root of c) and initialize it to the value of c.
t = c

# Repeat until t is accurate enough.
while abs(1 - c/(math.pow(t, k))) > (epsilon):
    # Improve t.
    t = (t - (math.pow(t, k) - c)) / (k * (math.pow(t, k - 1)))

# Write t.
stdio.writeln(t)
