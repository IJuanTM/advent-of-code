import os

import regex as re

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()

# ---------------------------------------------------------------- #

# define a list of worded numbers
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

numbers = []

for line in lines:
    # find all numbers in the line
    digits = [str(words.index(number) + 1) if number in words else number for number in re.findall(r'(?:one|two|three|four|five|six|seven|eight|nine|\d)', line, overlapped=True)]

    # get the first digit
    first_digit = int(digits[0])

    # append the first digit and the last digit (if there is one) to the list of numbers
    numbers.append(str(first_digit) + str(int(digits[-1]) if len(digits) > 1 else first_digit))

print(sum(map(int, numbers)))  # 56324
