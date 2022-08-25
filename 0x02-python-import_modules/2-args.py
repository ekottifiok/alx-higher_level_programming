#!/usr/bin/python3
from sys import argv


def main():
    i = len(argv) - 1
    print("{} {}{}".format(i,
                           'argument' if i == 1 else 'arguments',
                           '.' if i == 0 else ':'))
    if i != 0:
        for j in range(1, i+1):
            print("{}: {}".format(j, argv[j]))


if __name__ == '__main__':
    main()
