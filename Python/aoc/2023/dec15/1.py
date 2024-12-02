import os

# read the input
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    instructions = f.read().strip().split(",")


def hash(value: str):
    cur_value = 0
    for char in value:
        cur_value = (cur_value + ord(char)) * 17 % 256
    return cur_value


print(sum(hash(instruction) for instruction in instructions))  # 513643
