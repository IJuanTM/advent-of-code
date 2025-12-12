def part_1():
    present_sizes = []
    i = 0

    while len(present_sizes) < 6 and i < len(lines):
        if lines[i].endswith(':'):
            i += 1
            size = 0
            while i < len(lines) and lines[i] and not lines[i].endswith(':') and 'x' not in lines[i]:
                size += lines[i].count('#')
                i += 1
            present_sizes.append(size)
        else:
            i += 1

    count = 0
    while i < len(lines):
        if lines[i] and 'x' in lines[i] and ':' in lines[i]:
            delim = lines[i].index(':')
            w, h = map(int, lines[i][:delim].split('x'))
            presents = list(map(int, lines[i][delim + 2:].split()))

            total_area = sum(presents[j] * present_sizes[j] for j in range(len(presents)))

            if w * h >= total_area:
                count += 1
        i += 1

    return count


if __name__ == "__main__":
    import os

    EXPECTED = 454

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = [line.rstrip('\n') for line in f]

    result_1 = part_1()

    print(f"{result_1}")

    assert result_1 == EXPECTED, f"Part 1 failed: expected {EXPECTED}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED else 'too high'}"
