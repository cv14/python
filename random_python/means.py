# means.py: reads in positive real numbers from standard input and writes their
# geometric and harmonic means.

import math
import stdio

# Read floats from standard input into a list a.
a = stdio.readAllFloats()

# Define a variable n storing the length of a.
n = len(a)

# Define variables gm and hm to store the geometric and harmonic means of
# the numbers in a, with initial values 0.0.
gm = 1.0
hm = 0.0

# Iterate over the values in a and calculate their geometric and harmonic
# means. For geometric mean, consider taking logarithms to avoid overflow.
for v in a:
    gm = gm * v
    hm += 1/v


gm = math.pow(gm, 1.0/n)
hm = n/hm

# Write the results (geometric and harmonic means).
stdio.writef('geometric mean = %f, harmonic mean = %f\n', gm, hm)
