import stdio
import sys


# Returns the GCD of p and q, computed using Euclid's algorithm.
def _gcd(p, q):
    return p if q == 0 else _gcd(q, p % q)


class Rational:
    """
    Represents a rational number.
    """

    def __init__(self, x, y=1):
        """
        Constructs a new rational given its numerator and denominator.
        """

        if y == 0:
            raise ZeroDivisionError("Denominator of a rational\
                                      may not be zero.")
        else:
            d = _gcd(x, y)
            self._x = x / d
            self._y = y / d

    def __add__(self, other):
        """
        Returns the sum of self and other.
        """

        r = self._x * other._y + other._x * self._y
        s = self._y * other._y
        return Rational(r, s)

    def __sub__(self, other):
        """
        Returns the difference of self and other.
        """

        r = self._x * other._y - other._x * self._y
        s = self._y * other._y
        return Rational(r, s)

    def __mul__(self, other):
        """
        Returns the product of self and other.
        """

        r = self._x * other._x
        s = self._y * other._y
        return Rational(r, s)

    def __abs__(self):
        """
        Return the absolute value of self.
        """

        r = (self._x*self._x + self._y*self._y)**0.5
        return r

    def __str__(self):
        """
        Returns a string representation of self.
        """

        a, b = self._x, self._y
        if a == 0 or b == 1:
            return str(a)
        if b < 0:
            a *= -1
            b *= -1
        return str(a) + '/' + str(b)


# Test client [DO NOT EDIT]. Reads an integer n as command-line argument and
# prints the value of PI computed using Leibniz series:
#   PI/4 = 1 - 1/3 + 1/5 - 1/7 + ... + (-1)^n/(2n-1).
def main():
    n = int(sys.argv[1])
    total = Rational(0)
    sign = Rational(1)
    for i in range(1, n + 1):
        total += sign * Rational(1, 2 * i - 1)
        sign *= Rational(-1)
    stdio.writeln(4.0 * total._x / total._y)

if __name__ == '__main__':
    main()
