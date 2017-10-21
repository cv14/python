# edit_distance.py: Reads strings x and y from standard input and computes
# the edit-distance matrix opt. The program outputs x, y, the dimensions
# (number of rows and columns) of opt, and opt itself.

import stdarray
import stdio

# Read x and y.
x = stdio.readString()
y = stdio.readString()

# Create (M + 1) x (N + 1) matrix opt with elements initialized to 0, where
# M and N are lengths of x and y respectively.
m = len(x)
n = len(y)
opt = stdarray.create2D((m + 1), (n + 1), 0)

# Initialize opt[M][j] (j < N) and opt[i][N] (i < M) to appropriate values.
for i in range(n - 1, -1,-1):
    opt[m][i] = opt[m][i+1] + 2

for j in range(m - 1, -1,-1):
    opt[j][n] = opt[j+1][n] + 2

# Compute the rest of opt.
a1 = 0
b1 = 0

for j in range(n - 1, -1,-1):
    for i in range(m - 1, -1, -1):
        if(x[i] == y[j]):
           opt[i][j] = opt[i+1][j+1]
        else:
           val = opt[i+1][j+1]+1
           emptyX = opt[i][j+1] + 2
           emptyY = opt[i+1][j] + 2
           opt[i][j] = min(min(emptyX,emptyY),val)
           
# Write x, y, dimensions of opt, and opt.
stdio.writeln(x)
stdio.writeln(y)
stdio.writeln(str(m+1) + ' ' + str(n+1))
for i in range(0, m + 1):
    for j in range(0, n + 1):
        if j < n:
            stdio.writef("%3d ", opt[i][j])
        else:
            stdio.writef("%3d\n", opt[i][j])
