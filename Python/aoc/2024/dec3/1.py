import os
import re

# Read the file and calculate the sum of valid mul operations
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    print(sum(int(x) * int(y) for x, y in re.compile(r'mul\((\d+),(\d+)\)').findall(f.read())))  # 182780583
