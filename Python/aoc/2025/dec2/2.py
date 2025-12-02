import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    ranges = [tuple(map(int, r.split('-'))) for r in f.read().strip().split(',')]

total = sum(n for start, end in ranges for n in range(start, end + 1) if (s := str(n)) and any(len(s) % d == 0 and s == s[:len(s) // d] * d for d in range(2, len(s) + 1)))

print(total)  # 46270373595
