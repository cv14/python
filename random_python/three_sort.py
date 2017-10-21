# three_sort.py: Takes three integers as command-line arguments and prints
# them in ascending order, separated by spaces.

import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
stdio.write(min(x,y,z))
stdio.write(' ')
stdio.write(max(min(x,y), min(y, z), min(x,z)))
stdio.write(' ')
stdio.writeln(max(x,y,z))



