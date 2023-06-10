#!/usr/bin/python3
# This is a function that returns a tuple with the length
# of a string and its first character.

def multiple_returns(sentence):
    ret = (
            len(sentence),
            (None if len(sentence) == 0 else sentence[0])
    )
    return ret
