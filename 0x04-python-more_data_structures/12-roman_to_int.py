#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return None
    integer = 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    save = 0
    for n in reversed(roman_string):
        if n.upper() not in roman:
            return None
        n = roman[n.upper()]
        if n >= save:
            integer += n
        else:
            integer -= n
        save = n
    return integer
