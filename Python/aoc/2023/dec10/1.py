import os

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    pipes = f.read().splitlines()

# ---------------------------------------------------------------- #

directions = {"W": (-1, 0), "S": (0, 1), "E": (1, 0), "N": (0, -1)}

pipe_directions = {
    "|": {"S": "S", "N": "N"},
    "-": {"W": "W", "E": "E"},
    "L": {"S": "E", "W": "N"},
    "J": {"S": "W", "E": "N"},
    "7": {"N": "W", "E": "S"},
    "F": {"N": "E", "W": "S"},
}

opposite_direction = {"N": "S", "S": "N", "E": "W", "W": "E"}

start_x, start_y = next((x, y) for y, row in enumerate(pipes) if "S" in row for x, _ in enumerate(row) if row[x] == "S")

last_directions = []

for direction, (x_offset, y_offset) in directions.items():
    if direction in last_directions:
        continue

    step_counter = 1
    x = start_x + x_offset
    y = start_y + y_offset
    if x < 0 or y < 0 or pipes[y][x] == ".":
        continue

    while pipes[y][x] in pipe_directions:
        current_pipe_directions = pipe_directions[pipes[y][x]]
        if direction not in current_pipe_directions:
            break
        direction = current_pipe_directions[direction]
        x_offset, y_offset = directions[direction]
        x += x_offset
        y += y_offset
        step_counter += 1

    if pipes[y][x] == "S":
        last_directions.append(opposite_direction[direction])
        print(int(step_counter / 2))  # 6890
