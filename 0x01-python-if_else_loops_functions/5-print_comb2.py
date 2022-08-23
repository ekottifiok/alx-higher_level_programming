#!/usr/bin/python3
for i in range(99):
    if i == 98:
        print(i)
        break
    print(f"{i:02d}", end=", ")
