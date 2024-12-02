import os
import re

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()

# ---------------------------------------------------------------- #

numbers = []

for line in lines:
    # find all numbers in the line
    digits = re.findall(r'\d', line)

    # append the first digit and the last digit to the list of numbers
    numbers.append(digits[0] + digits[-1])

print(sum(map(int, numbers)))  # 55108
