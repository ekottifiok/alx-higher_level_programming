#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    func_dict = {'+': add, '-': sub, '*': mul, '/': div}
    symbol = argv[2]
    i1 = int(argv[1])
    i2 = int(argv[3])
    which_func = add
    try:
        which_func = func_dict[symbol]
    except (KeyError, ):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(i1, symbol, i2, which_func(i1, i2)))


if __name__ == '__main__':
    main()
