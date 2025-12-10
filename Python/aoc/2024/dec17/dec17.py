def part_1():
    a = int(lines[0].split(": ")[1])
    b = int(lines[1].split(": ")[1])
    c = int(lines[2].split(": ")[1])
    program = list(map(int, lines[4].split(": ")[1].split(",")))

    get_value = lambda x: x if x <= 3 else (a if x == 4 else b if x == 5 else c)

    ip = 0
    output = []

    while ip < len(program):
        opcode, operand = program[ip], program[ip + 1]
        if opcode == 0:
            a //= 2 ** get_value(operand)
        elif opcode == 1:
            b ^= operand
        elif opcode == 2:
            b = get_value(operand) % 8
        elif opcode == 3:
            ip = operand if a != 0 else ip + 2
        elif opcode == 4:
            b ^= c
        elif opcode == 5:
            output.append(get_value(operand) % 8)
        elif opcode == 6:
            b = a // 2 ** get_value(operand)
        elif opcode == 7:
            c = a // 2 ** get_value(operand)
        ip += 2 if opcode != 3 or a == 0 else 0

    return ",".join(map(str, output))


def part_2():
    program = list(map(int, lines[4].split(": ")[1].split(",")))

    def solve(pointer, result):
        if pointer < 0:
            return result

        for d in range(8):
            a, b, c = result << 3 | d, 0, 0
            output_value = None
            ip = 0

            while ip < len(program):
                opcode, operand = program[ip], program[ip + 1]
                value = 0

                if operand <= 3:
                    value = operand
                elif operand == 4:
                    value = a
                elif operand == 5:
                    value = b
                elif operand == 6:
                    value = c

                if opcode == 0:
                    a //= 2 ** value
                elif opcode == 1:
                    b ^= operand
                elif opcode == 2:
                    b = value % 8
                elif opcode == 3:
                    ip = operand if a != 0 else ip + 2
                    continue
                elif opcode == 4:
                    b ^= c
                elif opcode == 5:
                    output_value = value % 8
                    break
                elif opcode == 6:
                    b = a // 2 ** value
                elif opcode == 7:
                    c = a // 2 ** value

                ip += 2

            if output_value == program[pointer]:
                res = solve(pointer - 1, result << 3 | d)
                if res is not None:
                    return res

        return None

    return solve(len(program) - 1, 0)


if __name__ == "__main__":
    import os

    EXPECTED = ("3,1,4,3,1,7,1,6,3", 37221270076916)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.read().splitlines()

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
