def part_1(lines):
    items = [{i for i, c in enumerate(item) if c == '#'} for item in lines]
    return sum(not k & l for k in items for l in items) // 2


if __name__ == "__main__":
    import os

    EXPECTED = 3344

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.read().split('\n\n')

    result_1 = part_1(lines)

    assert result_1 == EXPECTED, f"Part 1 failed: expected {EXPECTED}, got {result_1}"

    print(f"{result_1}")
