import stdio
import sys


# Returns the domain type of the given URL.
def domain_type(URL):
    slash = URL.find('//', 0)
    dot = URL.find('.', slash + 1)
    dot2 = URL.find('.', dot + 1)
    end = URL.find('/', dot2)
    domain = URL[dot2 + 1:end]
    return domain


# Test client [DO NOT EDIT]. Reads a URL as command-line argument and prints
# its domain type.
def main():
    URL = sys.argv[1]
    stdio.writeln(domain_type(URL))

if __name__ == '__main__':
    main()
