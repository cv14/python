import stdio
import sys
from interval import Interval


class Rectangle:
    """
    Represents a rectangle as two (x and y) intervals.
    """

    def __init__(self, xint, yint):
        """
        Constructs a new rectangle given the x and y intervals.
        """

        self._xint = xint
        self._yint = yint

    def area(self):
        """
        Returns the area of self.
        """

        rx = self._xint._right - self._xint._left
        ry = self._yint._right - self._yint._left
        return rx * ry

    def perimeter(self):
        """
        Returns the perimeter of self.
        """

        rx = self._xint._right - self._xint._left
        ry = self._yint._right - self._yint._left
        rp = (2 * rx) + (2 * ry)
        return rp

    def contains(self, x, y):
        """
        Returns True if self contains the point (x, y) and False otherwise.
        """

        if (x and y) < self._yint._right and (x and y) > self._xint._left:
            return True
        else:
            return False

    def intersects(self, other):
        """
        Returns True if self intersects other and False othewise.
        """

        if other._yint._right > self._xint._left and\
           other._yint._right > self._yint._right and\
           self._yint._right >= other._xint._left:
            return True
        else:
            return False

    def __str__(self):
        """
        Returns a string representation of self.
        """

        r = '[' + str(self._xint._left) + ', ' + str(self._xint._right)\
                + ']' + ' x ' + '[' + str(self._yint._left) + ', '\
                + str(self._yint._right) + ']'
        return r


# Test client [DO NOT EDIT]. Reads a floats x and y from the command line and
# writes to standard output: all of the rectangles from standard input
# (each defined by two pairs of floats) that contain (x, y); and all pairs
# of rectangles from standard input that intersect one another.
def main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    rectangles = []
    while not stdio.isEmpty():
        left1 = stdio.readFloat()
        right1 = stdio.readFloat()
        left2 = stdio.readFloat()
        right2 = stdio.readFloat()
        rectangles += [Rectangle(Interval(left1, right1),
                                 Interval(left2, right2))]
    for i in range(len(rectangles)):
        stdio.writef('Area(%s) = %f\n', rectangles[i], rectangles[i].area())
        stdio.writef('Perimeter(%s) = %f\n', rectangles[i],
                     rectangles[i].perimeter())
        if rectangles[i].contains(x, y):
            stdio.writef('%s contains (%f, %f)\n', rectangles[i], x, y)
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if rectangles[i].intersects(rectangles[j]):
                stdio.writef('%s intersects %s\n',
                             rectangles[i], rectangles[j])

if __name__ == '__main__':
    main()
