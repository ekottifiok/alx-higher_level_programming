#!/usr/bin/python3

for i in range(1, 100):
    n = i
    # reverse the integer number using the while loop
    revs_number = 0
    while n > 0:
        # Logic
        remainder = n % 10
        revs_number = (revs_number * 10) + remainder
        n = n // 10
    if i == 89:
        print("{}".format(i))
        break
    if revs_number > i or i < 10:
        print("{:02d}".format(i), end=", ")
