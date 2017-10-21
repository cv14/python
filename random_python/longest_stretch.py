# longest_stretch.py: writes the longest contiguous sequence of equal
# integer values, from the sequence of integers read from the
# command line.

import stdio
import sys

# Create a list a consisting of the integers from the command line.
a = []
for v in sys.argv[1:]:
    a += [int(v)]


# Identify the starting position ms and length ml of the longest contiguous
# sequence of integers (ie, the longest stretch) from a.
s = 0   # current stretch start
l = 1   # current stretch length
ms = 0  # longest stretch start
ml = 0  # longest stretch length
for i in range(1, len(a)):
    # If a[i] is different from a[i - 1], then we have the start of a new
    # stretch. In that case: if l is greater than ml, set ms to s and ml to l;
    # then, unconditionally set s to i and l to 1. If a[i] is the same as
    # a[i - 1], increment l by 1.
    if (a[i] != a[i - 1]):
        if(l > ml):
            ms = s
            ml = l
        s = i
        l = 1

    if(a[i] == a[i -1]):
           l = l+1

# Again, if l is greater than ml, set ms to s and ml to l.
if(l > ml):
       ms = s
       ml = l

# Write the longest stretch from a, separating each by a space, and with a
# newline at the end.
for i in range(ms, ms + ml - 1):
    stdio.write(str(a[i]) + ' ')
stdio.write(a[ms + ml - 1])
stdio.writeln()
