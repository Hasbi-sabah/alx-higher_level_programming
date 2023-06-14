#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sorted_vals = dict(sorted(a_dictionary.items(), lambda x: x[1]))
    return list(sorted_vals)[-1]
