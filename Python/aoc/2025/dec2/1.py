import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    ranges = [tuple(map(int, r.split('-'))) for r in f.read().strip().split(',')]

total = sum(n for start, end in ranges for n in range(start, end + 1) if len(s := str(n)) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:])

print(total)  # 30599400849
