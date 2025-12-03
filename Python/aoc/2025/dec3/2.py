import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    banks = [line.strip() for line in f]

total = 0
for bank in banks:
    result = ''
    for length in range(12, 0, -1):
        digit = max(bank[:len(bank) - length + 1])
        bank = bank[bank.index(digit) + 1:]
        result += digit
    total += int(result)

print(total)  # 172886048065379
