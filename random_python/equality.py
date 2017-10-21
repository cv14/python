# equality.py: takes three integers as command-line arguments and writes
# "equal" if all three are equal, and "not equal" otherwise.

import stdio
import sys

# Get x, y, and z from command line, as ints.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# If x, y, and z are all equal, then write "equal". Otherwise,
# write "not equal".
if x == y and y == z and z == x:
    stdio.writeln('equal')
else:
    stdio.writeln('not equal')
