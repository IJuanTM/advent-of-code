import os
import re

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    schematics = f.read().splitlines()

# ---------------------------------------------------------------- #

# create a list of sets of adjacent coordinates
adj = [[[] for _ in range(len(schematics))] for _ in range(len(schematics))]

# find adjacent coordinates and store the corresponding numbers
for i in range(len(schematics)):
    # find all numbers in the line
    for match in re.finditer(r'\d+', schematics[i]):
        # iterate through the numbers
        for j in range(*match.span()):
            # iterate through the adjacent coordinates
            for k in range(-1, 2):
                # iterate through the adjacent coordinates
                for l in range(-1 if j == match.span()[0] else 0, 1 if j < match.span()[1] - 1 else 2):
                    # check if the number is surrounded by digits or dots (except for the number itself)
                    if 0 <= i + k < len(schematics) and 0 <= j + l < len(schematics) and schematics[i + k][j + l] == '*':
                        # store the number
                        adj[i + k][j + l].append(int(match.group()))

# calculate the sum of products of adjacent numbers and print it
print(sum(adj[x][y][0] * adj[x][y][1] for x in range(len(schematics)) for y in range(len(schematics)) if len(adj[x][y]) == 2))  # 82824352
