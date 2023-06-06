#!/usr/bin/python3
# This is a function that prints the last digit of a number.

def print_last_digit(number):
    n = abs(number) % 10
    print(n, end='')
    return n
