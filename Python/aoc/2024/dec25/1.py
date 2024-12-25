import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().split('\n\n')

items = [{i for i, c in enumerate(item) if c == '#'} for item in lines]

print(sum(not k & l for k in items for l in items) // 2)  # 3344