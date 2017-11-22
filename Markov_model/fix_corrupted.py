import stdio
import sys
from markov_model import markov_model


# Takes an integer k (model order) and a string s (noisy message) as
# command-line arguments, reads the input text from standard input, and
# prints out the most likely original string.
def main():
    k = int(sys.argv[1])
    s = sys.argv[2]
    t = sys.stdin.read()
    model = markov_model(t, k)
    stdio.writeln(model.replace_unknown(s))

if __name__ == '__main__':
    main()
