# five_per_row.py: writes the integers 101 to 200 with five numbers per line.

import stdio
import sys

# Iterate over the integers 101 to 201, and write five of them per row.
for i in range(101, 201):
    

    # If the integer is a multiple of 5, write the integer followed by a
    # new line. Otherwise, write the integer followed by a space.
    if i % 5 == 0:
        stdio.writeln(i)
    else:
        stdio.write(str(i) + ' ')
