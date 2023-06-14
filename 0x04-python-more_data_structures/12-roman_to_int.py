#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string and type(variable) != str:
        return None
    integer = 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    save = 0
    flag = 0
    for n in roman_string:
        if roman_string.index(n) == 0:
            save = roman[n]
            flag = 1
            continue
        n = roman[n]
        if flag:
            n, save = save, n
        if n >= save:
            integer += n
        else:
            integer -= save
            save = n
            flag = 0
    integer += save
    return abs(integer)
