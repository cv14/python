import stdio
import sys


# Return the number of zeros in s, computed recursively.
def zeros(s):
    if len(s) == 0:
        return 0
    if s[0] == '0':
        return 1 + zeros(s[1:])
    return zeros(s[1:])


# Return the number of ones in s, computed recursively.
def ones(s):
    if len(s) == 0:
        return 0
    if s[0] == '1':
        return 1 + ones(s[1:])
    return ones(s[1:])


# Test client [DO NOT EDIT]. Reads a string s from command line and prints the
# the number of zeros and ones in s, both computed recursively.
def main():
    s = sys.argv[1]
    stdio.writef('zeros = %d, ones = %d, total = %d\n',
                 zeros(s), ones(s), len(s))

if __name__ == '__main__':
    main()
