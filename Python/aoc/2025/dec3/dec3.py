def part_1():
    return sum(max(int(bank[i] + bank[j]) for i in range(len(bank)) for j in range(i + 1, len(bank))) for bank in banks)


def part_2():
    total = 0

    for bank in banks:
        result = ''
        for length in range(12, 0, -1):
            digit = max(bank[:len(bank) - length + 1])
            bank = bank[bank.index(digit) + 1:]
            result += digit
        total += int(result)

    return total


if __name__ == "__main__":
    import os

    EXPECTED = (17435, 172886048065379)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        banks = [line.strip() for line in f]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
