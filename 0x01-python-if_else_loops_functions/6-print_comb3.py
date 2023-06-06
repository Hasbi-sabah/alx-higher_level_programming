#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            if i * 10 + j != 89:
                print(f'{(i * 10 + j):02d}', end=', ')
            else:
                print("89")
