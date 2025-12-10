from math import prod


def part_1():
    total = sum(sum(int(lines_1[j][col]) for j in range(len(lines_1) - 1)) if lines_1[-1][col] == '+' else prod(int(lines_1[j][col]) for j in range(len(lines_1) - 1)) for col in range(len(lines_1[0])))
    return total


def part_2():
    width = max(len(line) for line in lines_2)
    lines = [line.ljust(width) for line in lines_2]

    total = 0
    col = width - 1
    nums = []

    while col >= 0:
        num_str = ''.join(lines[row][col] for row in range(len(lines) - 1) if lines[row][col] != ' ')
        if num_str:
            nums.append(int(num_str))

        op = lines[-1][col]
        if op in '+*':
            total += sum(nums) if op == '+' else prod(nums)
            nums = []
            col -= 1

        col -= 1

    return total


if __name__ == "__main__":
    import os

    EXPECTED = (4309240495780, 9170286552289)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines_1 = [line.split() for line in f]

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines_2 = [line.rstrip('\n') for line in f]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
