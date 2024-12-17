import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()

program = list(map(int, lines[4].split(": ")[1].split(",")))


def solve(pointer, result):
    if pointer < 0:
        print(result)
        return True

    for d in range(8):
        A, B, C = result << 3 | d, 0, 0
        output_value = None
        ip = 0

        while ip < len(program):
            opcode, operand = program[ip], program[ip + 1]
            value = 0

            if operand <= 3:
                value = operand
            elif operand == 4:
                value = A
            elif operand == 5:
                value = B
            elif operand == 6:
                value = C

            if opcode == 0:
                A //= 2 ** value
            elif opcode == 1:
                B ^= operand
            elif opcode == 2:
                B = value % 8
            elif opcode == 3:
                ip = operand if A != 0 else ip + 2
                continue
            elif opcode == 4:
                B ^= C
            elif opcode == 5:
                output_value = value % 8
                break
            elif opcode == 6:
                B = A // 2 ** value
            elif opcode == 7:
                C = A // 2 ** value

            ip += 2

        if output_value == program[pointer] and solve(pointer - 1, result << 3 | d):
            return True

    return False


solve(len(program) - 1, 0)  # 37221270076916
