import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    grid, moves = f.read().split('\n\n')


def move(grid_dict, p, d):
    p += d
    if all([
        grid_dict[p] != '[' or move(grid_dict, p + 1, d) and move(grid_dict, p, d),
        grid_dict[p] != ']' or move(grid_dict, p - 1, d) and move(grid_dict, p, d),
        grid_dict[p] != 'O' or move(grid_dict, p, d), grid_dict[p] != '#']):
        grid_dict[p], grid_dict[p - d] = grid_dict[p - d], grid_dict[p]
        return True


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
print(int(ans.real + ans.imag * 100))  # 1415498
