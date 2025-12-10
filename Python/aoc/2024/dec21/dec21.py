def solve(layers):
    key_coords = {c: (x, y) for y, row in enumerate([" ^A", "<v>"]) for x, c in enumerate(row)}
    leg_lengths = {(0, ki, kf): 1 for ki in key_coords for kf in key_coords}

    for layer in range(1, layers + 1):
        if layer == layers:
            key_coords = {c: (x, y) for y, row in enumerate(["789", "456", "123", " 0A"]) for x, c in enumerate(row)}

        for ki, (xi, yi) in key_coords.items():
            for kf, (xf, yf) in key_coords.items():
                hor_ks = ('>' if xf > xi else '<') * abs(xf - xi)
                ver_ks = ('^' if yf < yi else 'v') * abs(yf - yi)

                if (xf, yi) != key_coords[' ']:
                    fewest_hor_first = sum(leg_lengths[(layer - 1, ki, kf)] for ki, kf in zip('A' + hor_ks + ver_ks + 'A', hor_ks + ver_ks + 'A'))
                else:
                    fewest_hor_first = float('inf')

                if (xi, yf) != key_coords[' ']:
                    fewest_ver_first = sum(leg_lengths[(layer - 1, ki, kf)] for ki, kf in zip('A' + ver_ks + hor_ks + 'A', ver_ks + hor_ks + 'A'))
                else:
                    fewest_ver_first = float('inf')

                leg_lengths[(layer, ki, kf)] = min(fewest_hor_first, fewest_ver_first)

    result = 0
    for code in input_text.splitlines():
        fewest_presses = sum(leg_lengths[(layers, ki, kf)] for ki, kf in zip('A' + code, code))
        result += fewest_presses * int(code[:-1])

    return result


def part_1():
    return solve(3)


def part_2():
    return solve(26)


if __name__ == "__main__":
    import os

    EXPECTED = (107934, 130470079151124)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        input_text = f.read()

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
