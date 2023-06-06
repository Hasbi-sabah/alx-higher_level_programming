#!/usr/bin/python3
# This is a program that prints the ASCII alphabet,
# in reverse order, alternating lowercase and uppercase.

for i in range(90, 64, -1):
    print("{}".format(chr(i + 32) if (i % 2 == 0) else chr(i)), end='')
