import operator
import stdio
import sys


# Returns a list containing the keys of the dictionary st in reverse order
# of the values of the dictionary.
def keys(st):
    a = sorted(st.items(), key=operator.itemgetter(1), reverse=True)
    return [v[0] for v in a]


# Returns a dictionary whose keys are the words from the given list of words
# and values are the corresponding frequencies.
def count_word_frequencies(words):
    st = {}
    for i in words:
        st[str(i)] = st.get(i, 0) + 1
    return st


# Writes (in reverse order of values) the key-value pairs of the dictionary
# st to standard output, one per line, and with a ' -> ' between a key and
# the corresponding value.
def write_word_frequencies(st):
    st2 = keys(st)
    for i in range(len(st2)):
        stdio.write((st2[i] + ' -> '))
        stdio.writeln(st[st2[i]])


# Test client [DO NOT EDIT]. Reads words fro  m standard input and prints
# the words along with their frequencies, in reverse order of frequencies.
def main():
    words = stdio.readAllStrings()
    write_word_frequencies(count_word_frequencies(words))

if __name__ == '__main__':
    main()
