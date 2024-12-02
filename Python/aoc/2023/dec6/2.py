import os

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    # set the time and distance values for the first two lines
    time, dist = ["".join(filter(None, next(f).split(":")[1].strip().split(" "))) for _ in range(2)]

# ---------------------------------------------------------------- #

# print the sum of the values that are greater than the record
print(sum(i * (int(time) - i) > int(dist) for i in range(int(time))))  # 41513103
