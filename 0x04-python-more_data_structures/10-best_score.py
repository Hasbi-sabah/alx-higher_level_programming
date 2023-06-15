#!/usr/bin/python3
# This is a function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sorted_vals = dict(sorted(a_dictionary.items(), key=lambda x: x[1]))
    return list(sorted_vals)[-1]
