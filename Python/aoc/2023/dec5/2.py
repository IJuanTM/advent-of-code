import os
import re

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()

# ---------------------------------------------------------------- #

maps = []

for line in lines[2:]:
    if 'map' in line:
        maps.append(dict())
    elif line != '':
        destination, source, length = [int(value) for value in line.split()]
        maps[-1][range(source, source + length)] = range(destination, destination + length)


def reverse_lookup_seed(location: int) -> int:
    value = location

    for current_map in reversed(maps):
        for source_range, destination_range in current_map.items():
            if value in destination_range:
                value = source_range.start + (value - destination_range.start)
                break

    return value


initial_seed_data = [int(seed) for seed in re.findall(r'\d+', lines[0])]

seed_ranges = [range(start, start + length) for start, length in zip(initial_seed_data[::2], initial_seed_data[1::2])]

location = 0

while True:
    potential_seed = reverse_lookup_seed(location)

    if any(potential_seed in seed_range for seed_range in seed_ranges):
        print(location)  # 52510809
        break

    location += 1
