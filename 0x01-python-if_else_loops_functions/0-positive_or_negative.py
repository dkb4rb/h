#!/usr/bin/python3

"""Print the last digits"""

import random
number = random.randit(-10, 10)

if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")