from collections import defaultdict
from itertools import pairwise


def part_1():
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

    return bananas


def part_2():
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

    return max(bananas.values())


if __name__ == "__main__":
    import os

    EXPECTED = (12979353889, 1449)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
