# prime_counter.py: takes an integer N as command-line argument and writes the
# number of primes less than or equal to N.

import stdio
import sys
import math

# Get N from command line, as an int.
N = int(sys.argv[1])

# Define primes to store the number of primes <= N.
primes = 0

# Iterate over integers 2 to N (inclusive).
for i in range(2, N):
    # Define a variable j to store the potential divisors of i, and initialize
    # it to 2.
    j = 2

    # Test if i is prime. Repeat as long as j is <= square root of i.
    while j <= math.sqrt(i):
        # If i is divisible by j, it is not a prime so exit this inner loop.
        if i % j == 0:
            break

        # Increment j.
        j += 1

    # If j is > square root of i, then we got here by exhausting the while
    # loop, and i is therefore a prime. So increment primes by one.
    if j > math.sqrt(i):
        primes += 1

# Write primes.
stdio.writeln(primes)
