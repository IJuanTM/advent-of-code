def part_1(sections):
    total = 0

    for section in sections:
        lines = section.splitlines()

        a_x, a_y = [int(value[2:]) for value in lines[0].split(": ")[1].split(", ")]
        b_x, b_y = [int(value[2:]) for value in lines[1].split(": ")[1].split(", ")]
        p_x, p_y = [int(value[2:]) for value in lines[2].split(": ")[1].split(", ")]

        min_cost = float('inf')
        found = False

        for x in range(101):
            for y in range(101):
                if x * a_x + y * b_x == p_x and x * a_y + y * b_y == p_y:
                    cost = 3 * x + y
                    min_cost = min(min_cost, cost)
                    found = True

        if found:
            total += min_cost

    return total


def part_2(sections):
    offset = 10 ** 13
    total = 0

    for section in sections:
        lines = section.splitlines()

        a_x, a_y = [int(value[2:]) for value in lines[0].split(": ")[1].split(", ")]
        b_x, b_y = [int(value[2:]) for value in lines[1].split(": ")[1].split(", ")]
        p_x, p_y = [int(value[2:]) for value in lines[2].split(": ")[1].split(", ")]

        if offset:
            p_x += offset
            p_y += offset

        i = a_x * b_y - a_y * b_x
        j = p_x * b_y - p_y * b_x
        k = a_x * p_y - a_y * p_x

        if j % i == 0 and k % i == 0:
            total += 3 * (j // i) + (k // i)

    return total


if __name__ == "__main__":
    import os

    EXPECTED = (31552, 95273925552482)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        sections = f.read().strip().split("\n\n")

    result_1 = part_1(sections)
    result_2 = part_2(sections)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
