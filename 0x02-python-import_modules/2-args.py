#!/usr/bin/python3
# This is a program that prints the number of and the list of its arguments.

from sys import argv
if __name__ == "__main__":
    print("{} {}{}{}".format(len(argv) - 1,
          "argument", "s" if len(argv) - 1 != 1 else "",
                             ":" if len(argv) - 1 > 0 else "."))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
