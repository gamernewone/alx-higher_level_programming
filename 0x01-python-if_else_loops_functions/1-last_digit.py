#!/usr/bin/python3
# Author Ridy rich

import random
number = random.randint(-10000, 10000)
digit = str(number)
last_digit = int(digit[-1])

print(f"Last digit of {number:d} is {last_digit:d} and is ", end="")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")