# three_dice.py: writes the sum of three random integers between 1 and 6, such
# as you might get when rolling three dice.

import random
import stdio

a = random.randrange(1, 6)
b = random.randrange(1, 6)
c = random.randrange(1, 6)
a = a+b+c
stdio.writeln(a)
