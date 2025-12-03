import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    banks = [line.strip() for line in f]

total = sum(max(int(bank[i] + bank[j]) for i in range(len(bank)) for j in range(i + 1, len(bank))) for bank in banks)

print(total)  # 17435
