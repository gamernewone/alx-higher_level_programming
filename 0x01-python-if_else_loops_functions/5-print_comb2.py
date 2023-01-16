#!/usr/bin/python3
# Print from 0 to 99 with 2 number

for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
