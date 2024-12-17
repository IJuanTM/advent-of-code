import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()

A = int(lines[0].split(": ")[1])
B = int(lines[1].split(": ")[1])
C = int(lines[2].split(": ")[1])
program = list(map(int, lines[4].split(": ")[1].split(",")))

get_value = lambda x: x if x <= 3 else (A if x == 4 else B if x == 5 else C)

ip = 0
output = []

while ip < len(program):
    opcode, operand = program[ip], program[ip + 1]
    if opcode == 0:
        A //= 2 ** get_value(operand)
    elif opcode == 1:
        B ^= operand
    elif opcode == 2:
        B = get_value(operand) % 8
    elif opcode == 3:
        ip = operand if A != 0 else ip + 2
    elif opcode == 4:
        B ^= C
    elif opcode == 5:
        output.append(get_value(operand) % 8)
    elif opcode == 6:
        B = A // 2 ** get_value(operand)
    elif opcode == 7:
        C = A // 2 ** get_value(operand)
    ip += 2 if opcode != 3 or A == 0 else 0

print(",".join(map(str, output)))  # 3,1,4,3,1,7,1,6,3
