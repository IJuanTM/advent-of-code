import os

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

# ---------------------------------------------------------------- #

# set the current position to the start
cur = 'AAA'

i = 0

# iterate through the instructions
for i in range(1000000):
    # get the instruction
    cur = maps[cur][data[i % len(data)]]

    # if we're at the end, break
    if cur[2] == 'Z':
        break

# print the number of steps
print(i + 1)  # 20569
