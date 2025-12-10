def part_1():
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

    return total_sum


def part_2():
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

            for op in ['||', '+', '*']:
                next_carry = carry
                if op == '+':
                    next_carry = carry + number
                elif op == '*':
                    next_carry = carry * number
                elif op == '||':
                    next_carry = int(str(carry) + str(number))
                stack.append((next_carry, rest))

        if is_true:
            total_sum += wanted

    return total_sum


if __name__ == "__main__":
    import os

    EXPECTED = (28730327770375, 424977609625985)

    equations = []
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        for line in f:
            l, r = line.strip().split(": ")
            equations.append((int(l), list(map(int, r.split()))))

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
