#!/usr/bin/python3

import string
from unittest import result


def roman_to_int(roman_string):
    result = 0
    prev = 0
    chain = 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if isinstance(roman_string, string):
        for str in roman_string:
            str_int = 0 if str not in roman.keys() else roman.get(str)
            if prev == str_int:
                # if chain == 0:
                #     chain = prev
                chain += str_int
            elif prev != 0 and prev < str_int:
                result -= prev + chain
                result += str_int - prev
                chain = 0
            elif result < str_int and result != 0:
                result = str_int - result
            else:
                result += str_int + chain
                chain = 0
            prev = str_int
        if chain != 0:
            result += chain
        return result if result > 0 else 0
    return None
