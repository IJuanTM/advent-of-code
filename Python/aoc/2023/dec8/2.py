import os

import numpy as np

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    # get the data
    data = f.readline().strip()

    # get the indices of the R's
    hits = [i for i, char in enumerate(data) if char == 'R']

    # convert the data to a list of 1's and 0's
    data = [1 if i in hits else 0 for i in range(len(data))]

    # skip the next line
    f.readline()

    # create a dictionary of the maps
    maps = {line[0]: line[1:] for line in [line.strip().replace("=", "").replace("(", "").replace(")", "").replace(",", "").split() for line in f]}

# get the starting curs
curs = [c for c in maps.keys() if c[2] == 'A']

metadata = []

# iterate through the instructions
for cur in curs:
    i = 0

    # iterate through the instructions
    for i in range(1000000):
        # get the instruction
        cur = maps[cur][data[i % len(data)]]

        # if we're at the end, break
        if cur[2] == 'Z':
            break

    # append the number of steps
    metadata.append(i + 1)

# print the number of steps
print(np.lcm.reduce(np.array(metadata, dtype=np.int64)))  # 21366921060721
