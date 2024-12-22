import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.readlines()

bananas = 0

for line in lines:
    s = int(line)
    nums = [s]

    for _ in range(2000):
        s ^= s << 6 & 0xFFFFFF
        s ^= s >> 5 & 0xFFFFFF
        s ^= s << 11 & 0xFFFFFF
        nums.append(s)

    bananas += nums[-1]

print(bananas)  # 12979353889