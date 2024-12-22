import os
from collections import defaultdict
from itertools import pairwise

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.readlines()

bananas = defaultdict(int)

for line in lines:
    s = int(line)
    nums = [s]
    for _ in range(2000):
        s ^= s << 6 & 0xFFFFFF
        s ^= s >> 5 & 0xFFFFFF
        s ^= s << 11 & 0xFFFFFF
        nums.append(s)

    diffs = [b % 10 - a % 10 for a, b in pairwise(nums)]

    seen = set()
    for i in range(len(nums) - 4):
        pat = tuple(diffs[i:i + 4])
        if pat not in seen:
            bananas[pat] += nums[i + 4] % 10
            seen.add(pat)

print(max(bananas.values()))  # 1449