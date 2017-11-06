import math
import random
import ring_buffer
import stdarray
import stdio
import sys
import stdrandom

# Sampling rate.
SPS = 44100


# Create and return a guitar string of the given frequency, using a sampling
# rate given by SPS. A guitar string is represented as a ring buffer of
# of capacity N (SPS divided by frequency, rounded up to the nearest integer),
# with all values initialized to 0.0.
def create(frequency):
    capacity = int(SPS/frequency)
    a = ring_buffer.create(capacity)
    a[1] = len(a[0])
    for i in range(len(a[0])):
        a[0][i] = 0
    return a

# Create and return a guitar string whose size and initial values are given
# by the list init. For debugging


def create_from_samples(init):
    capacity = len(init)
    a = ring_buffer.create(capacity)
    a[1] = len(a[0])
    for i in range(len(a[0])):
        a[0][i] = init[i]
    return a

# Pluck the given guitar string by replacing the buffer with white noise.
# Change every value in buffer to value btwn -.5 and .5 .


def pluck(string):
    for i in range(len(string[0])):
        #every element in buffer has to be randon # between -.5, .5
        a = stdrandom.uniformFloat(-.5, .6)
        string[0][i] = a


# Advance the simulation one time step on the given guitar string by applying
# the Karplus-Strong update

def tic(string):
    a = ring_buffer.dequeue(string)
    b = ring_buffer.peek(string)
    c = ((a+b)/2) * .996
    ring_buffer.enqueue(string, c)


# Return the current sample from the given guitar string. gives 1st element.
# just call peek
def sample(string):
    a = ring_buffer.peek(string)
    return a


# Test client [DO NOT EDIT].
def main():
    N = int(sys.argv[1])
    samples = [.2, .4, .5, .3, -.2, .4, .3, .0, -.1, -.3]
    test_string = create_from_samples(samples)

    for t in range(N):
        stdio.writef('%6d %8.4f\n', t, sample(test_string))
        tic(test_string)


if __name__ == '__main__':
    main()
