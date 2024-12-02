import os

# read the input and store the platform
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    platform = tuple(tuple(line.strip()) for line in f)


def north_tilt(platform):
    res = [list(row) for row in platform]
    for i, row in enumerate(res):
        for j, cell in enumerate(row):
            if cell == 'O':
                row_index = i
                while row_index > 0 and res[row_index - 1][j] == '.':
                    row_index -= 1
                res[i][j], res[row_index][j] = res[row_index][j], res[i][j]
    return tuple(tuple(row) for row in res)


def west_tilt(platform):
    res = [list(row) for row in platform]
    for i, row in enumerate(res):
        for j, cell in enumerate(row):
            if cell == 'O':
                col_index = j
                while col_index > 0 and res[i][col_index - 1] == '.':
                    col_index -= 1
                res[i][j], res[i][col_index] = res[i][col_index], res[i][j]
    return tuple(tuple(row) for row in res)


def south_tilt(platform):
    res = [list(row) for row in platform]
    for i in range(len(res) - 1, -1, -1):
        for j, cell in enumerate(res[i]):
            if cell == 'O':
                row_index = i
                while row_index < len(res) - 1 and res[row_index + 1][j] == '.':
                    row_index += 1
                res[i][j], res[row_index][j] = res[row_index][j], res[i][j]
    return tuple(tuple(row) for row in res)


def east_tilt(platform):
    res = [list(row) for row in platform]
    for i, row in enumerate(res):
        for j in range(len(row) - 1, -1, -1):
            if row[j] == 'O':
                col_index = j
                while col_index < len(row) - 1 and res[i][col_index + 1] == '.':
                    col_index += 1
                res[i][j], res[i][col_index] = res[i][col_index], res[i][j]
    return tuple(tuple(row) for row in res)


cache = {}
is_cycle = False


def tilt_cycle_cached(platform):
    global cache, is_cycle

    def tilt_cycle(platform):
        platform = north_tilt(platform)
        platform = west_tilt(platform)
        platform = south_tilt(platform)
        platform = east_tilt(platform)
        return platform

    if platform in cache:
        is_cycle = True
        return cache[platform]
    else:
        result = tilt_cycle(platform)
        cache[platform] = result
        return result


# find the beginning of the cycle
while not is_cycle:
    platform = tilt_cycle_cached(platform)

start = platform

# find the cycle length
cycle_length = 1
platform = tilt_cycle_cached(platform)

while platform != start:
    platform = tilt_cycle_cached(platform)
    cycle_length += 1

# find the final platform
start_to_cycle_length = len(cache) + 1
remaining_cycles = (1_000_000_000 - start_to_cycle_length) % cycle_length

platform = start

for _ in range(remaining_cycles):
    platform = tilt_cycle_cached(platform)

# calculate the result
result = sum(len(platform) - i for i, row in enumerate(platform) for j, cell in enumerate(row) if cell == 'O')

print(result)
