import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    data = f.read()

total = 0
position = 0
enabled = True

for mul_match in re.compile(r'mul\((\d+),(\d+)\)').finditer(data):
    while position < mul_match.start():
        control = re.compile(r"(do\(\)|don't\(\))").search(data, position)
        if control and control.start() < mul_match.start():
            enabled = control.group() == "do()"
            position = control.end()
        else:
            break

    if enabled:
        total += int(mul_match.group(1)) * int(mul_match.group(2))

print(total)  # 90772405
