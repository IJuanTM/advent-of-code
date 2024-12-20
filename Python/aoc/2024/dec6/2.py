import os
from typing import List


def look_ahead(data, pos):
    return data[pos[0]][pos[1]] if 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]) else None


def rotate_right(direction: List[int]):
    direction[:] = [direction[1], -direction[0]]
    return direction


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        grid = [list(line) for line in f.read().strip().splitlines()]

    a, b = next((i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == '^')
    direction = [-1, 0]

    count = 0

    while 0 <= a < len(grid) and 0 <= b < len(grid[0]):
        while look_ahead(grid, [a + direction[0], b + direction[1]]) == '#':
            rotate_right(direction)

        ahead_a, ahead_b = a + direction[0], b + direction[1]

        if look_ahead(grid, [ahead_a, ahead_b]) is None:
            break

        if grid[ahead_a][ahead_b] == '.':
            grid[ahead_a][ahead_b] = '#'

            temp_a, temp_b, temp_direction = a, b, direction[:]

            path = set()

            while 0 <= temp_a < len(grid) and 0 <= temp_b < len(grid[0]):
                while look_ahead(grid, [temp_a + temp_direction[0], temp_b + temp_direction[1]]) == '#':
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

            grid[ahead_a][ahead_b] = ''

        a += direction[0]
        b += direction[1]

    print(count)
