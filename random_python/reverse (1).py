import stdio
import sys


# Returns the reverse of the string s, computed recursively.
def reverse(s):
    if len(s) == 0:
        return ' '
    return s[-1] + reverse(s[:-1])



# Test client [DO NOT EDIT]. Read a string s from command line and prints its
# reverse, computed recursively.
def main():
    s = sys.argv[1]
    stdio.writeln(reverse(s))

if __name__ == '__main__':
    main()
