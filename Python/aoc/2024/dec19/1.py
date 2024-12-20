import os
from functools import cache

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    patterns, _, *data = f.read().splitlines()


@cache
def count(data):
    return data == '' or sum(count(data.removeprefix(pattern)) for pattern in patterns.split(', ') if data.startswith(pattern))


print(sum(map(bool, map(count, data))))  # 251
