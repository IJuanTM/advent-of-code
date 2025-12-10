def part_1():
    new_grid = [row[:] for row in grid]
    a, b = next([i, j] for i, row in enumerate(new_grid) for j, cell in enumerate(row) if cell == '^')
    direction = [-1, 0]
    count = 0

    while 0 <= a < len(new_grid) and 0 <= b < len(new_grid[0]):
        if new_grid[a][b] != 'X':
            count += 1
            new_grid[a][b] = 'X'

        if 0 <= a + direction[0] < len(new_grid) and 0 <= b + direction[1] < len(new_grid[0]):
            next_field = new_grid[a + direction[0]][b + direction[1]]
        else:
            next_field = None

        if next_field == '#':
            direction.reverse()
            direction[1] *= -1

        a += direction[0]
        b += direction[1]

    return count


def look_ahead(data, pos):
    return data[pos[0]][pos[1]] if 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]) else None


def rotate_right(direction):
    direction[:] = [direction[1], -direction[0]]
    return direction


def part_2():
    new_grid = [row[:] for row in grid]
    a, b = next((i, j) for i, row in enumerate(new_grid) for j, val in enumerate(row) if val == '^')
    direction = [-1, 0]
    count = 0

    while 0 <= a < len(new_grid) and 0 <= b < len(new_grid[0]):
        while look_ahead(new_grid, [a + direction[0], b + direction[1]]) == '#':
            rotate_right(direction)

        ahead_a, ahead_b = a + direction[0], b + direction[1]

        if look_ahead(new_grid, [ahead_a, ahead_b]) is None:
            break

        if new_grid[ahead_a][ahead_b] == '.':
            new_grid[ahead_a][ahead_b] = '#'

            temp_a, temp_b, temp_direction = a, b, direction[:]
            path = set()

            while 0 <= temp_a < len(new_grid) and 0 <= temp_b < len(new_grid[0]):
                while look_ahead(new_grid, [temp_a + temp_direction[0], temp_b + temp_direction[1]]) == '#':
                    seen = (temp_a, temp_b, temp_direction[0], temp_direction[1])

                    if seen in path:
                        count += 1
                        break

                    path.add(seen)
                    rotate_right(temp_direction)
                else:
                    temp_a += temp_direction[0]
                    temp_b += temp_direction[1]
                    continue
                break

            new_grid[ahead_a][ahead_b] = ''

        a += direction[0]
        b += direction[1]

    return count


if __name__ == "__main__":
    import os

    EXPECTED = (4789, 1304)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        grid = [list(line) for line in f.readlines()]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
