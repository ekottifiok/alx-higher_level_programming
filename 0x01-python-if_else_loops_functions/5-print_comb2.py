#!/usr/bin/python3
for i in range(99):
    if i == 98:
        print("{}".format(i))
        break
    print("{:02d}".format(i), end=", ")
