from operator import and_, or_, xor

AND, OR, XOR = and_, or_, xor


def part_1(lines):
    for line in lines:
        parts = line.split()

        if len(parts) == 5:
            a, x, b, _, c = parts
            exec(f'{c} = lambda: {x}({a}(), {b}())', globals())
        else:
            exec(line.replace(':', '= lambda:'), globals())

    return sum(eval(f'z{i:02}() << {i}') for i in range(46))


def part_2(lines):
    lines = [l.split() for l in lines if '->' in l]

    r = lambda c, y: any(y == x and c in (a, b) for a, x, b, _, _ in lines)

    result = sorted(c for a, x, b, _, c in lines if
                    x == "XOR" and all(d[0] not in 'xyz' for d in (a, b, c)) or
                    x == "AND" and not "x00" in (a, b) and r(c, 'XOR') or
                    x == "XOR" and not "x00" in (a, b) and r(c, 'OR') or
                    x != "XOR" and c[0] == 'z' and c != "z45")

    return ','.join(result)


if __name__ == "__main__":
    import os

    EXPECTED = (41324968993486, "bmn,jss,mvb,rds,wss,z08,z18,z23")

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()

    result_1 = part_1(lines)
    result_2 = part_2(lines)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
