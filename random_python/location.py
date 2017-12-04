import math
import stdio
import sys


class Location:
    """
    Represents a location on Earth.
    """

    def __init__(self, lat, lon):
        """
        Constructs a new location given its latitude and longitude values.
        """

        self._lat = lat
        self._lon = lon

    def distanceTo(self, other):
        """
        Returns the great-circle distance between self and other.
        """

        self._lat = math.radians(self._lat)
        self._lon = math.radians(self._lon)
        other._lat = math.radians(other._lat)
        other._lon = math.radians(other._lon)
        lond = self._lon - other._lon
        l = math.sin(self._lat) * math.sin(other._lat)
        m = math.cos(self._lat) * math.cos(other._lat) * math.cos(lond)
        dist = 111 * math.acos(l + m)
        return math.degrees(dist)

    def __str__(self):
        """
        Returns a string representation of self.
        """

        return '(' + str(self._lat) + ', ' + str(self._lon) + ')'


# Test client [DO NOT EDIT]. Reads floats lat1, lon1, lat2, lon2 from command
# representing two locations on Earth, constructs two Location objects from
# them, and prints them along with the great-circle distance between the two.
def main():
    lat1, lon1, lat2, lon2 = map(float, sys.argv[1:])
    loc1 = Location(lat1, lon1)
    loc2 = Location(lat2, lon2)
    stdio.writeln('loc1 = ' + str(loc1))
    stdio.writeln('loc2 = ' + str(loc2))
    stdio.writeln('d(loc1, loc2) = ' + str(loc1.distanceTo(loc2)))

if __name__ == '__main__':
    main()
