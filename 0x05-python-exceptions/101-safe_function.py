#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return float(fct(*args))
    except IndexError:
        print("Exception: list index out of range", file=stderr)
        return None
    except ValueError:
        print("Exception: ValueError", file=stderr)
        return None
    except ZeroDivisionError:
        print("Exception: division by zero", file=stderr)
        return None
    except TypeError:
        print("Exception: the type is wrong", file=stderr)
        return None
