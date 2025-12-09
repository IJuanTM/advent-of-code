def part_1(data):
    even = []
    odd = []
    pos = 0

    for i, c in enumerate(data):
        c_range = list(range(pos, pos + int(c)))
        pos += int(c)

        if i % 2 == 0:
            even.append(c_range)
        else:
            odd.append(c_range)

    odd_list = [i for sublist in odd for i in sublist]

    for y in reversed(even):
        for x in reversed(range(len(y))):
            if odd_list and y[x] > odd_list[0]:
                y[x] = odd_list[0]
                odd_list = odd_list[1:]

    return sum(i * j for i, even_range in enumerate(even) for j in even_range)


def part_2(data):
    even = []
    odd = []
    pos = 0

    for i, c in enumerate(data):
        current_range = list(range(pos, pos + int(c)))
        pos += int(c)

        if i % 2 == 0:
            even.append(current_range)
        else:
            odd.append(current_range)

    for y in reversed(range(len(even))):
        for x in range(len(odd)):
            if len(odd[x]) >= len(even[y]) and even[y][0] > odd[x][0]:
                even[y] = odd[x][:len(even[y])]
                odd[x] = odd[x][len(even[y]):]

    return sum(i * j for i, even_range in enumerate(even) for j in even_range)


if __name__ == "__main__":
    import os

    EXPECTED = (6331212425418, 6363268339304)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        data = f.read().strip()

    result_1 = part_1(data)
    result_2 = part_2(data)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
