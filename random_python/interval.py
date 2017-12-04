import stdio
import sys


class Interval:
    """
    Represents a 1-dimensional interval [left, right].
    """

    def __init__(self, left, right):
        """
        Constructs a new interval given its left and right bounds.
        """

        self._left = left
        self._right = right

    def contains(self, x):
        """
        Returns True if self contains the point x and False otherwise.
        """

        if x < self._right and x > self._left:
            return True
        else:
            return False

    def intersects(self, other):
        """
        Returns True if self intersects other and False othewise.
        """

        if other._right > self._left and other._right > self._right and \
           self._right >= other._left:
            return True
        else:
            return False

    def __str__(self):
        """
        Returns a string representation of self.
        """

        strin = '[' + str(self._left) + ', ' + str(self._right) + ']'
        return strin


# Test client [DO NOT EDIT]. Reads a float x from the command line and
# writes to standard output: all of the intervals from standard input
# (each defined by a pair of floats) that contain x; and all pairs
# of intervals from standard input that intersect one another.
def main():
    x = float(sys.argv[1])
    intervals = []
    while not stdio.isEmpty():
        left = stdio.readFloat()
        right = stdio.readFloat()
        intervals += [Interval(left, right)]
    for i in range(len(intervals)):
        if intervals[i].contains(x):
            stdio.writef('%s contains %f\n', intervals[i], x)
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i].intersects(intervals[j]):
                stdio.writef('%s intersects %s\n', intervals[i], intervals[j])

if __name__ == '__main__':
    main()
