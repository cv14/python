import stdio
import sys


# Return the Euclidean distance between x and y, calculated as as the square
# root of the sums of the squares of the differences between corresponding
# entries. You may assume that x and y have the same length.
def distance(x, y):
    total = 0
    for i in range(len(x)):
        total += (x[i] - y[i]) * (x[i] - y[i])
    total = total ** 0.5
    return total

# Test client [DO NOT EDIT]. Reads an integer n as command-line argument, and
# then calculates and prints the Euclidean distance between two n-dimensional
# vectors read from standard input.
def main():
    n = int(sys.argv[1])
    x = [stdio.readFloat() for i in range(n)]
    y = [stdio.readFloat() for i in range(n)]
    stdio.writeln(distance(x, y))

if __name__ == '__main__':
    main()
