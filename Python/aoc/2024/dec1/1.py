import os

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.readlines()

# ---------------------------------------------------------------- #

# parse and sort the input into two lists
left_list, right_list = [], []
for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# sort both lists
left_list.sort()
right_list.sort()

# calculate and print the total distance
print(sum(abs(left - right) for left, right in zip(left_list, right_list)))  # 1941353