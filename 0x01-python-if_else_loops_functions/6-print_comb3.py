#!/usr/bin/python3
# This is a program that prints all
# possible different combinations of two digits.

for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            if i * 10 + j != 89:
                print("{:02d}".format(i * 10 + j), end=', ')
            else:
                print("89")
