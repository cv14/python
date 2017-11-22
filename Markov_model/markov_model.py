"""
markov_model.py

A data type that represents a Markov model of order k from a given text string.
"""

import stdio
import stdrandom
import sys


class markov_model(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Creates a Markov model of order k from given text. Assumes that text
        has length at least k.
        """

        self.k = k
        self.st = {}
        circ_text = text + text[:k]
        for i in range(len(circ_text) - k):
            self.st.setdefault(circ_text[i:i+k], {})
            self.st[circ_text[i:i+k]].setdefault(circ_text[k+i], 0)
            self.st[circ_text[i:i+k]][circ_text[k+i]] += 1

    def order(self):
        """
        Returns order k of Markov model.
        """
        return self.k

    def kgram_freq(self, kgram):
        """
        Returns number of occurrences of kgram in text. Raises an error if
        kgram is not of length k.
        """

        if self.k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self.k))

        if kgram not in self.st:
                return 0
        a = self.st[kgram].values()
        a = sum(a)
        return a

    def char_freq(self, kgram, c):
        """
        Returns number of times character c follows kgram. Raises an error if
        kgram is not of length k.
        """

        if self.k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self.k))
        if kgram not in self.st:
            return 0
        if c not in self.st[kgram]:
            return 0
        return self.st[kgram][c]

    def rand(self, kgram):
        """
        Returns a random character following kgram. Raises an error if kgram
        is not of length k or if kgram is unknown.
        """

        if self.k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self.k))
        if not kgram in self.st:
            raise ValueError('Unknown kgram ' + kgram)

        a = self.st[kgram].values()
        s = sum(a)
        for i in range(len(a)):
            a[i] = a[i]/float(s)
        d = stdrandom.discrete(a)
        a = self.st[kgram].keys()
        return a[d]

    def gen(self, kgram, T):
        """
        Generates and returns a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k characters of the
        generated string is the argument kgram. Assumes that T is at least k.
        """
        text = kgram
        while len(text) < T:
            text += self.rand(text[-self.order():])
        return text

    def replace_unknown(self, corrupted):
        argmax = lambda a: a.index(max(a))
        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                t = {}
                char = self.st[corrupted[i - self.k:i]].keys()
                for key in char:
                    rep = self.order() + 1
                    for q in range(rep):
                        kgram = corrupted[i - self.k + q:i +
                                          q].replace('~', key)
                        character = corrupted[i + q].replace('~', key)
                        if kgram in self.st:
                            p = (self.char_freq(kgram, character) /
                                 float(self.kgram_freq(kgram)))
                        else:
                            p = 0
                        if key in t:
                            t[key] *= p
                        else:
                            t.setdefault(key, p)
                x = argmax(t.values())
                t_keys = t.keys()
                original += t_keys[x]
            else:
                original += corrupted[i]
        return original


def main():
    """
    Test client [DO NOT EDIT].
    """

    text = 'banana'
    k = 2
    model = markov_model(text, k)
    stdio.writef('text: %s, k = %d\n', text, k)
    stdio.writef('freq(\'an\', \'a\')  = %d\n', model.char_freq('an', 'a'))
    stdio.writef('freq(\'na\', \'b\')  = %d\n', model.char_freq('na', 'b'))
    stdio.writef('freq(\'na\', \'a\')  = %d\n', model.char_freq('na', 'a'))
    stdio.writef('freq(\'na\')       = %d\n', model.kgram_freq('na'))
    stdio.writeln()
    text = 'one fish two fish red fish blue fish'
    k = 4
    model = markov_model(text, k)
    stdio.writef('text: %s, k = %d\n', text, k)
    stdio.writef('freq(\'ish \', \'r\') = %d\n', model.char_freq('ish ', 'r'))
    stdio.writef('freq(\'ish \', \'0\') = %d\n', model.char_freq('ish ', '0'))
    stdio.writef('freq(\'ish \')      = %d\n', model.kgram_freq('ish '))
    stdio.writef('freq(\'tuna\')      = %d\n', model.kgram_freq('tuna'))
    stdio.writeln()
    text = 'gagggagaggcgagaaa'
    k = 2
    model = markov_model(text, k)
    stdio.writef('text: %s, k = %d\n', text, k)
    stdio.writef('freq(\'aa\', \'a\') = %d\n', model.char_freq('aa', 'a'))
    stdio.writef('freq(\'ga\', \'g\') = %d\n', model.char_freq('ga', 'g'))
    stdio.writef('freq(\'gg\', \'c\') = %d\n', model.char_freq('gg', 'c'))
    stdio.writef('freq(\'ag\')      = %d\n', model.kgram_freq('ag'))
    stdio.writef('freq(\'cg\')      = %d\n', model.kgram_freq('cg'))
    stdio.writef('freq(\'gc\')      = %d\n', model.kgram_freq('gc'))

if __name__ == '__main__':
    main()
