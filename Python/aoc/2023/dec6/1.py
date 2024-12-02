import os

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    races = [list(map(int, line.split()[1:])) for line in f.read().splitlines()]

# ---------------------------------------------------------------- #

total = 1

for race in zip(races[0], races[1]):
    # multiply the total by the sum of the values that are greater than the record
    total *= sum(1 for i in range(1, race[0]) if i * (race[0] - i) > race[1])

print(total)  # 1159152
