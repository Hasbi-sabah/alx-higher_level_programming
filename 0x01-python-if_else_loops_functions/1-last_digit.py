#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if number < 0:
    n = -n
line = "Last digit of {} is {} and is {}"
if n > 5:
    print(line.format(number, n, "greater than 5"))
elif n < 6 and n != 0:
    print(line.format(number, n, "less than 6 and not 0"))
else:
    print(line.format(number, n, "0"))
