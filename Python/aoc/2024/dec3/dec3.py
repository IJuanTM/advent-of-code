import re


def part_1(data):
    return sum(int(x) * int(y) for x, y in re.compile(r'mul\((\d+),(\d+)\)').findall(data))


def part_2(data):
    total = 0
    position = 0
    enabled = True

    for mul_match in re.compile(r'mul\((\d+),(\d+)\)').finditer(data):
        while position < mul_match.start():
            control = re.compile(r"(do\(\)|don't\(\))").search(data, position)
            if control and control.start() < mul_match.start():
                enabled = control.group() == "do()"
                position = control.end()
            else:
                break

        if enabled:
            total += int(mul_match.group(1)) * int(mul_match.group(2))

    return total


if __name__ == "__main__":
    import os

    EXPECTED = (182780583, 90772405)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        data = f.read()

    result_1 = part_1(data)
    result_2 = part_2(data)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
