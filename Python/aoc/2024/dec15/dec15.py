def move(grid_dict, p, d):
    p += d
    if all([
        grid_dict[p] != '[' or move(grid_dict, p + 1, d) and move(grid_dict, p, d),
        grid_dict[p] != ']' or move(grid_dict, p - 1, d) and move(grid_dict, p, d),
        grid_dict[p] != 'O' or move(grid_dict, p, d), grid_dict[p] != '#']):
        grid_dict[p], grid_dict[p - d] = grid_dict[p - d], grid_dict[p]
        return True


def part_1(grid, moves):
    cells = {i + j * 1j: c for j, r in enumerate(grid.split()) for i, c in enumerate(r)}
    pos, = [p for p in cells if cells[p] == '@']

    for m in moves.replace('\n', ''):
        direction = {'<': -1, '>': +1, '^': -1j, 'v': +1j}[m]
        C = cells.copy()

        if move(cells, pos, direction):
            pos += direction
        else:
            cells = C

    ans = sum(pos for pos in cells if cells[pos] in 'O[')
    return int(ans.real + ans.imag * 100)


def part_2(grid, moves):
    cells = grid.translate(str.maketrans({'#': '##', '.': '..', 'O': '[]', '@': '@.'}))
    cells = {i + j * 1j: c for j, r in enumerate(cells.split()) for i, c in enumerate(r)}
    pos, = [p for p in cells if cells[p] == '@']

    for m in moves.replace('\n', ''):
        direction = {'<': -1, '>': +1, '^': -1j, 'v': +1j}[m]
        C = cells.copy()

        if move(cells, pos, direction):
            pos += direction
        else:
            cells = C

    ans = sum(pos for pos in cells if cells[pos] in 'O[')
    return int(ans.real + ans.imag * 100)


if __name__ == "__main__":
    import os

    EXPECTED = (1415498, 1432898)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        grid, moves = f.read().split('\n\n')

    result_1 = part_1(grid, moves)
    result_2 = part_2(grid, moves)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
