# gcd.py: takes two integers x and y as command-line arguments and
# writes their greatest common divisor (gcd) computed using
# Euclid's Algorithm.

import stdio
import sys

# Get x and y from command line, as ints.
x = int(sys.argv[1])
y = int(sys.argv[2])

# Repeat as long as x is not divisible by y.
while x % y != 0  :
    # Set r to be the remainder of x divided by y; x to y; and y to r.
    r = x % y
    x = y
    y = r 

# Write y (the GCD of x and y).
stdio.writeln(y)
