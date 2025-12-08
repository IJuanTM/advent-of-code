def part_1(grid):
    start_col = grid[0].index('S')
    beams = {start_col}
    splits = 0

    for row in range(1, len(grid)):
        new_beams = set()
        for col in beams:
            if grid[row][col] == '^':
                splits += 1
                if col > 0:
                    new_beams.add(col - 1)
                if col < len(grid[row]) - 1:
                    new_beams.add(col + 1)
            else:
                new_beams.add(col)
        beams = new_beams

    return splits


def part_2(grid):
    start_col = grid[0].index('S')
    positions = {start_col: 1}

    for row in range(1, len(grid)):
        new_positions = {}
        for col, count in positions.items():
            if grid[row][col] == '^':
                if col > 0:
                    new_positions[col - 1] = new_positions.get(col - 1, 0) + count
                if col < len(grid[row]) - 1:
                    new_positions[col + 1] = new_positions.get(col + 1, 0) + count
            else:
                new_positions[col] = new_positions.get(col, 0) + count
        positions = new_positions

    return sum(positions.values())


if __name__ == "__main__":
    import os

    EXPECTED = (1662, 40941112789504)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        grid = [line.rstrip('\n') for line in f]

    result_1 = part_1(grid)
    result_2 = part_2(grid)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
