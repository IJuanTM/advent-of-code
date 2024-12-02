import os
import re

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()

# ---------------------------------------------------------------- #

maps = []

for line in lines[2:]:
    if 'map' in line:
        maps.append({})
    elif line != '':
        destination, source, length = map(int, line.split())
        maps[-1][range(source, source + length)] = range(destination, destination + length)


def lookup_location(initial_value: int) -> int:
    value = initial_value

    for current_map in maps:
        value = next((destination_range.start + (value - source_range.start) for source_range, destination_range in current_map.items() if value in source_range), value)

    return value


print(min([lookup_location(seed) for seed in [int(seed) for seed in re.findall(r'\d+', lines[0])]]))  # 662197086
