import os

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()

# ---------------------------------------------------------------- #

sum = 0

for line in lines:
    # count the number of words in the second part of the line that are in the first part of the line
    count = len(set(line.split('|')[0].split(':')[1].split()) & set(line.split('|')[1].split()))

    # if the count is greater than 0, add 2^(count - 1) to the sum
    if count > 0:
        sum += pow(2, count - 1)

print(sum)  # 24542
