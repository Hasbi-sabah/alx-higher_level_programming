#!/usr/bin/python3
# This is a program that imports all functions
# from the file calculator_1.py and handles basic operations.

from sys import argv
import calculator_1 as calc
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    print("{} {} {} =".format(a, op, b), end=' ')
    if op == '+':
        print("{}".format(calc.add(a, b)))
    elif op == '-':
        print("{}".format(calc.sub(a, b)))
    elif op == '*':
        print("{}".format(calc.mul(a, b)))
    else:
        print("{}".format(calc.div(a, b)))
