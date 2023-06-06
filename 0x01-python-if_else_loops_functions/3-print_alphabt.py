#!/usr/bin/python3
# This program that prints the ASCII alphabet, in lowercase,
# except the letters q and e

for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end='')
