#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end=' ')
if (number < 0):
    last_number = -((-1 * number) % 10)
else:
    last_number = number % 10
print(f"{last_number}", end=' ')
if (last_number == 0):
    print("and is 0")
elif (last_number > 5):
    print("and is greater than 5")
elif (last_number < 6):
    print("and is less than 6 and not 0")
