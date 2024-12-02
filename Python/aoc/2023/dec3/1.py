import os
import re

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    schematics = f.read().splitlines()

# ---------------------------------------------------------------- #

sum = 0

# iterate through the schematics
for i in range(len(schematics)):
    # find all numbers in the line
    for match in re.finditer(r'\d+', schematics[i]):
        try:
            # check if the number is surrounded by digits or dots
            for j in range(*match.span()):
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        # check if the number is surrounded by digits or dots (except for the number itself) and assert that it is
                        assert not (0 <= i + k < len(schematics) and 0 <= j + l < len(schematics) and not schematics[i + k][j + l].isdigit() and schematics[i + k][j + l] != '.')
        except:
            # sum the number
            sum += int(match.group())

print(sum)  # 556057
