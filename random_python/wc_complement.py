import stdio
import sys


# Returns the Watson-Crick complement of the given DNA string.
def wc_complement(dna):
    for x in range(len(dna)):
        if dna[x] == 'A' or dna[x] == 'G' and (dna[x] == 'T') or dna[x] == 'C':
            dna = dna.replace('A', 't')
            dna = dna.replace('G', 'c')
            dna = dna.replace('T', 'a')
            dna = dna.replace('C', 'g')
    return dna.upper()


# Test client [DO NOT EDIT]. Reads a DNA string as command-line argument and
# prints its Watson-Crick complement.
def main():
    dna = sys.argv[1]
    stdio.writeln(wc_complement(dna.upper()))

if __name__ == '__main__':
    main()
