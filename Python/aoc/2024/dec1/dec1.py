from collections import Counter


def part_1():
    left_list, right_list = [], []

    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    return sum(abs(left - right) for left, right in zip(left_list, right_list))


def part_2():
    left_list, right_list = [], []

    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    return sum(left * Counter(right_list)[left] for left in left_list)


if __name__ == "__main__":
    import os

    EXPECTED = (1941353, 22539317)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
