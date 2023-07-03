#!/usr/bin/python3
from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
n = argv[1]
if type(n) is not int:
    print('N must be a number')
    exit(1)
if n < 4:
    print('N must be at least 4')
    exit(1)
exit(69)
