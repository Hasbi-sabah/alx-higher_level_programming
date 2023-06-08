#!/usr/bin/python3
# This is a program that imports functions
# from the file add_0.py and does some Maths.

import calculator_1 as c1
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, c1.add(a, b)))
    print("{} + {} = {}".format(a, b, c1.sub(a, b)))
    print("{} + {} = {}".format(a, b, c1.mul(a, b)))
    print("{} + {} = {}".format(a, b, c1.div(a, b)))
