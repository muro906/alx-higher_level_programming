#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = 0
if number < 0:
    digit = abs(number) % 10
    print(f"Last digit of {number} is {-digit} and is less than 6 and not 0")
else:
    digit = number % 10
    if digit > 5:
        print(f"Last digit of {number} is {digit} and is greater than 5")
    elif digit == 0:
        print(f"Last digit of {number} is {digit} and is 0")
    else:
        print(f"Last digit of {number} is {digit} and is less than 6 and not 0")