import z3


def part_1():
    total = 0

    for line in lines:
        lights_part = line.split('[')[1].split(']')[0]
        target = [1 if c == '#' else 0 for c in lights_part]
        n = len(target)

        buttons_part = line.split(']')[1].split('{')[0].strip()
        buttons = []
        i = 0
        while i < len(buttons_part):
            if buttons_part[i] == '(':
                j = i + 1
                while buttons_part[j] != ')':
                    j += 1
                button = [int(x) for x in buttons_part[i + 1:j].split(',')]
                buttons.append(button)
                i = j + 1
            else:
                i += 1

        min_presses = float('inf')

        for mask in range(1 << len(buttons)):
            state = [0] * n
            presses = 0

            for i in range(len(buttons)):
                if mask & (1 << i):
                    presses += 1
                    for light in buttons[i]:
                        state[light] ^= 1

            if state == target:
                min_presses = min(min_presses, presses)

        total += min_presses

    return total


def part_2():
    total = 0

    for line in lines:
        joltage_part = line.split('{')[1].split('}')[0]
        target = [int(x) for x in joltage_part.split(',')]

        buttons_part = line.split(']')[1].split('{')[0].strip()
        buttons = []
        i = 0
        while i < len(buttons_part):
            if buttons_part[i] == '(':
                j = i + 1
                while buttons_part[j] != ')':
                    j += 1
                button = [int(x) for x in buttons_part[i + 1:j].split(',')]
                buttons.append(button)
                i = j + 1
            else:
                i += 1

        presses = [z3.Int(f"p{i}") for i in range(len(buttons))]
        optimizer = z3.Optimize()

        for counter_idx, target_val in enumerate(target):
            optimizer.add(z3.Sum([presses[b_idx] for b_idx, button in enumerate(buttons) if counter_idx in button]) == target_val)

        optimizer.add([p >= 0 for p in presses])
        optimizer.minimize(z3.Sum(presses))
        optimizer.check()

        model = optimizer.model()
        total += sum(model[v].as_long() for v in presses)

    return total


if __name__ == "__main__":
    import os

    EXPECTED = (452, 17424)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = [line.strip() for line in f]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
