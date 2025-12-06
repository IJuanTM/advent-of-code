import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    ranges = sorted(tuple(map(int, line.split('-'))) for line in f.read().strip().split('\n\n')[0].split('\n'))

count = 0
current_start, current_end = ranges[0]

for start, end in ranges[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        count += current_end - current_start + 1
        current_start, current_end = start, end

count += current_end - current_start + 1

print(count)  # 344378119285354
