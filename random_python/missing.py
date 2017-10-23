# missing.py: takes an integer N as command-line argument, reads in N - 1
# distinct integers between 1 and N from standard input, and writes the
# missing number.

import stdarray
import stdio
import sys

# Get N from command line, as an int.
N = int(sys.argv[1])

# Define a list a of N + 1 booleans, with each element initialized to False.
a = stdarray.create1D(N + 1, False)

# Read N - 1 distinct integers between 1 and N from standard input, and
# for each such integer x, set a[x] to True, meaning x was found.
for i in range(1, N):
    x = stdio.readInt()
    if(x >= 1 and x <= N):
        a[x] = True

# Iterate over a[1:] and write index of the False element, since that is the
# missing number.
for i in range(1, N + 1):
    if not a[i]:
        stdio.writeln(i)
