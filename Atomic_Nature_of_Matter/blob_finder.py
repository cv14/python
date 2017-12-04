import luminance
import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture


class BlobFinder:
    """
    A data type for identifying blobs in a picture.
    """

    def __init__(self, pic, tau):
        """
        Constructs a blob finder to find blobs in the picture pic, using
        a luminance threshold tau.
        """

        # Initialize an empty list for the blobs in pic.
        self._blobs = []

        # Create a 2D list of booleans called marked, having the same
        # dimensions as pic.
        self._marked = stdarray.create2D(pic.width(), pic.height(), False)

        # Enumerate the pixels of pic, and for each pixel (i, j):
        # 1. Create a Blob object called blob.
        # 2. Call _findBead() with the right arguments.
        # 3. Add blob to _blobs if it has a non-zero mass.\
        for i in range(pic.width()):
            for j in range(pic.height()):
                blob = Blob()
                self._findBlob(pic, tau, i, j, self._marked, blob)
                if blob.mass() > 0:
                    self._blobs += [blob]

    def _findBlob(self, pic, tau, i, j, marked, blob):
        """
        Identifies a blob using depth-first search. The parameters are
        the picture (pic), luminance threshold (tau), pixel column (i),
        pixel row (j), 2D boolean matrix (marked), and the blob being
        identified (blob).
        """

        # Base case: return if pixel (i, j) is out of bounds, or if is
        # is marked, or if its luminance is less than tau.
        if i < 0 or i >= pic.width():
            return
        if j < 0 or j >= pic.height():
            return
        if marked[i][j]:
            return
        if luminance.luminance(pic.get(i, j)) < tau:
            return
        # Mark the pixel.
        marked[i][j] = True

        # Add the pixel to blob.
        blob.add(i, j)

        # Recursively call _findBead() on the N, E, W, S pixels.
        self._findBlob(pic, tau, i+1, j, marked, blob)
        self._findBlob(pic, tau, i, j+1, marked, blob)
        self._findBlob(pic, tau, i, j-1, marked, blob)
        self._findBlob(pic, tau, i-1, j, marked, blob)

    def getBeads(self, P):
        """
        Returns a list of all beads with >= P pixels.
        """
        templist = []
        for i in range(len(self._blobs)):
            if self._blobs[i].mass() >= P:
                templist += [self._blobs[i]]
        return templist

    def __len__(self):
        count = 0
        for i in range(len(self._blobs)):
            count += 1
        return count

# Takes an integer P, a float tau, and the name of a JPEG file as
# command-line arguments; prints out all of the beads with at least P
# pixels; and then prints out all of the blobs (beads with at least 1 pixel).


def main():
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    jpic = sys.argv[3]
    jpic = Picture(jpic)
    b = BlobFinder(jpic, tau)
    stdio.writeln(str(len(b.getBeads(P))) + ' Beads:')
    for i in b.getBeads(P):
        stdio.writeln(i)
    stdio.writeln(str(len(b)) + ' Blobs:')
    for i in b.getBeads(1):
        stdio.writeln(i)

if __name__ == '__main__':
    main()
