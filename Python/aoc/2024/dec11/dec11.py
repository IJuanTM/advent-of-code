from collections import Counter, defaultdict


def solve(stones, blinks):
    for _ in range(blinks):
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

    return sum(stones.values())


def part_1(stones):
    return solve(stones.copy(), 25)


def part_2(stones):
    return solve(stones.copy(), 75)


if __name__ == "__main__":
    import os

    EXPECTED = (202019, 239321955280205)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        stones = Counter(map(int, f.read().strip().split()))

    result_1 = part_1(stones)
    result_2 = part_2(stones)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
