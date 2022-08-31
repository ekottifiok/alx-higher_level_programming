#!/usr/bin/python3

def best_score(a_dictionary):

    if isinstance(a_dictionary, dict) or len(a_dictionary) > 0:
        score = -99999999
        for value in a_dictionary.values():
            if value > score:
                score = value

        return score
    return None
