import os
from collections import Counter, defaultdict

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    stones = Counter(map(int, f.read().strip().split()))

for _ in range(75):
    new_stones = defaultdict(int)

    for stone, count in stones.items():
        stone_str = str(stone)
        n = len(stone_str)

        if stone == 0:
            children = [1]
        elif n % 2 == 0:
            mid = n // 2
            children = [int(stone_str[:mid]), int(stone_str[mid:])]
        else:
            children = [stone * 2024]

        for child in children:
            new_stones[child] += count

    stones = new_stones

print(sum(stones.values()))  # 239321955280205
