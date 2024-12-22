import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    INPUT = f.read()

KEY_COORDS = {c: (x, y) for y, row in enumerate([" ^A", "<v>"]) for x, c in enumerate(row)}
leg_lengths = {(0, ki, kf): 1 for ki in KEY_COORDS for kf in KEY_COORDS}

for layer in range(1, 4):
    if layer == 3:
        KEY_COORDS = {c: (x, y) for y, row in enumerate(["789", "456", "123", " 0A"]) for x, c in enumerate(row)}

    for ki, (xi, yi) in KEY_COORDS.items():
        for kf, (xf, yf) in KEY_COORDS.items():
            hor_ks = ('>' if xf > xi else '<') * abs(xf - xi)
            ver_ks = ('^' if yf < yi else 'v') * abs(yf - yi)

            if (xf, yi) != KEY_COORDS[' ']:
                fewest_hor_first = sum(leg_lengths[(layer - 1, ki, kf)] for ki, kf in zip('A' + hor_ks + ver_ks + 'A', hor_ks + ver_ks + 'A'))
            else:
                fewest_hor_first = float('inf')

            if (xi, yf) != KEY_COORDS[' ']:
                fewest_ver_first = sum(leg_lengths[(layer - 1, ki, kf)] for ki, kf in zip('A' + ver_ks + hor_ks + 'A', ver_ks + hor_ks + 'A'))
            else:
                fewest_ver_first = float('inf')

            leg_lengths[(layer, ki, kf)] = min(fewest_hor_first, fewest_ver_first)

result = 0
for code in INPUT.splitlines():
    fewest_presses = sum(leg_lengths[(3, ki, kf)] for ki, kf in zip('A' + code, code))
    result += fewest_presses * int(code[:-1])

print(result)  # 107934