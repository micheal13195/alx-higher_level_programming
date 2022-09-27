#!/usr/bin/python3
import random
number = random.randint(-10, 10)
x = number
if x > 0:
    print('{:d} is positive'.format(number))
elif x == 0:
    print('{:d} is zero'.format(number))
else:
    print('{:d} is negative'.format(number))
