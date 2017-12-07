import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture
from instream import InStream
import stddraw


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and prints out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    fnames = sys.argv[4:len(sys.argv)]
    for i in range(len(fnames) - 1):
        pic1 = Picture(fnames[i])
        pic2 = Picture(fnames[i+1])
        b1 = BlobFinder(pic1, tau)
        b2 = BlobFinder(pic2, tau)
        beads1 = b1.getBeads(P)
        beads2 = b2.getBeads(P)
        for j in range(len(beads2)):
            shortest = 0
            t = True
            for k in range(len(beads1)):
                d = beads2[j].distanceTo(beads1[k])
                if d <= delta and t:
                    shortest = d
                    t = False
                elif d <= delta and d <= shortest:
                    shortest = d
            if shortest > 0:
                stdio.writef('%.4f\n', shortest)

if __name__ == '__main__':
    main()
