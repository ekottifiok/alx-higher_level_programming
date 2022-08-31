#!/usr/bin/python3

def best_score(a_dictionary):

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    score = None
    min_score = -9999999999999
    for key in a_dictionary.keys():
        value = a_dictionary.get(key)
        if value > min_score:
            min_score = value
            score = key

    return score
