import stdio
import sys


# Returns True if pwd is a valid password and False otherwise.
def is_valid(pwd):
    if len(pwd) < 8:
        return False
    valid = [False] * 4
    for i in range(len(pwd)):
        if pwd[i].isupper():
            valid[0] = True
        if pwd[i].islower():
            valid[1] = True
        if pwd[i].isdigit():
            valid[2] = True
        if not pwd[i].isalnum():
            valid[3] = True
    if valid == [True] * 4:
        return True
    else:
        return False


# Test client [DO NOT EDIT3]. Reads a password string as command-line argument
# and prints True if it's valid and False otherwise.
def main():
    pwd = sys.argv[1]
    stdio.writeln(is_valid(pwd))

if __name__ == '__main__':
    main()
