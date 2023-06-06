#!/usr/bin/python3
# This is a function that prints
# the numbers from 1 to 100 separated by a space
# or "Fizz" for a multiple of 3 or "Bizz" for a multiple of 5,
# or "FizzBizz" for both.

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz", end=' ')
            elif i % 3 == 0:
                print("Fizz", end=' ')
            elif i % 5 == 0:
                print("Buzz", end=' ')
        else:
            print(i, end=' ')
