import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    parts = f.read().strip().split('\n\n')
    ranges = [tuple(map(int, line.split('-'))) for line in parts[0].split('\n')]
    ids = [int(line) for line in parts[1].split('\n')]

count = sum(1 for i in ids if any(start <= i <= end for start, end in ranges))

print(count)  # 888
