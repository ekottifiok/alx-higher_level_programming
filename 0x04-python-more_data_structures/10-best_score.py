#!/usr/bin/python3

def best_score(a_dictionary):

    if isinstance(a_dictionary, dict):
        score = -99999999
        for value in a_dictionary.values():
            if value > score:
                score = value

        return score
    return None
