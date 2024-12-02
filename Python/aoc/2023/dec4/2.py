import os

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()

# ---------------------------------------------------------------- #

total = 0

# initialize a list of cards with 1 card
cards = [1] * len(lines)

for index, line in enumerate(lines):
    # count the number of words in the second part of the line that are in the first part of the line
    count = len([number for number in line.split('|')[1].split() if number in line.split('|')[0].split(':')[1].split()])

    # add the number of cards to the next card
    for i in range(count):
        cards[index + i + 1] += cards[index]

    # add the score to the total
    total += pow(2, count - 1)

print(sum(cards))  # 8736438
