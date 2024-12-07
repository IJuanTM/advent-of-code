import os

equations = []

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    for line in f:
        l, r = line.strip().split(": ")
        equations.append((int(l), list(map(int, r.split()))))

total_sum = 0

for wanted, numbers in equations:
    stack = [(0, numbers)]
    is_true = False

    while stack:
        carry, remaining = stack.pop()

        if carry > wanted:
            continue
        if not remaining:
            if carry == wanted:
                is_true = True
            continue

        number, *rest = remaining

        stack.append((carry + number, rest))
        stack.append((carry * number, rest))

    if is_true:
        total_sum += wanted

print(total_sum)  # 28730327770375