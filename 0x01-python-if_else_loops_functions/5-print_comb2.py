#!/usr/bin/python3
# This is a program that prints numbers from 0 to 99.

for i in range(0, 100):
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
