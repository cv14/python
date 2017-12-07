import math
import stdio


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():
    P = 0.5e-6
    R = 8.31457
    N = 9.135e-4
    CONVERSION = 0.175e-6
    T = 297
    d_list = stdio.readAllFloats()
    d_sum = 0.0
    n = len(d_list)
    for distance in d_list:
        d_sum += math.pow(distance * CONVERSION, 2)

    D = d_sum / (2 * n)
    k = (6 * math.pi * D * N * P) / T
    Na = R / k
    stdio.writef("Boltzman = %.6e\n", k)
    stdio.writef("Avogadro = %.6e\n", Na)

if __name__ == '__main__':
    main()
