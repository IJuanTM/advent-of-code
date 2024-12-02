import os

# read the input again
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    instructions = f.read().strip().split(",")


def hash(value: str):
    cur_value = 0
    for char in value:
        cur_value = (cur_value + ord(char)) * 17 % 256
    return cur_value


boxes = [{} for _ in range(256)]
for instruction in instructions:
    if "-" in instruction:
        label = instruction.split("-")[0]
        boxes[hash(label)].pop(label, -1)
    else:
        label, number = instruction.split("=")
        boxes[hash(label)][label] = int(number)

power = 0
for box_index, box in enumerate(boxes):
    for lens_index, (k, v) in enumerate(box.items()):
        power += (box_index + 1) * (lens_index + 1) * v

print(power)  # 265345
