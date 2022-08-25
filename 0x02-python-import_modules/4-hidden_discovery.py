#!/usr/bin/python3
import hidden_4


def main():
    for s in dir(hidden_4):
        if "__" in s:
            continue
        print("{}".format(s))


if __name__ == '__main__':
    main()
