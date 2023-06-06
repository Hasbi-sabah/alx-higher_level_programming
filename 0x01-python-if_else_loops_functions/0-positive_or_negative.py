#!/usr/bin/python3
# This program generates a random number,
# and checks if it's positive or negative.

import random
number = random.randint(-10, 10)
if number > 0:
    print(f'{number:d} is positive')
elif number < 0:
    print(f'{number:d} is negative')
else:
    print(f'{number:d} is zero')
