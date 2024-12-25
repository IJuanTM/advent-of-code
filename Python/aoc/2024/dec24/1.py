import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.readlines()

for line in lines:
    parts = line.split()

    if len(parts) == 5:
        a, x, b, _, c = parts
        exec(f'{c} = lambda: {x}({a}(), {b}())')
    else:
        exec(line.replace(':', '= lambda:'))

print(sum(eval(f'z{i:02}() << {i}') for i in range(46)))  # 41324968993486