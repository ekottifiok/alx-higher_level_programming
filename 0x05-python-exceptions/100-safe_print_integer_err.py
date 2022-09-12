#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except IndexError:
        print("Exception: IndexError", file=stderr)
        return False
    except ValueError:
        print("Exception: ValueError", file=stderr)
        return False
    return True
