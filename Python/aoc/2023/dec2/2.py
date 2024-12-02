import os

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    games = f.read().splitlines()

# ---------------------------------------------------------------- #

sum = 0

for game in games:
    lowest_numbers = [0, 0, 0]

    for set in [set.strip() for set in game.split(':')[1].strip().split(';')]:
        for cube in [cube.strip().split(' ') for cube in set.split(',')]:
            # get the color and the number
            color, number = cube[1], int(cube[0])

            # check if the number is the lowest for the color
            if color == 'red' and number > lowest_numbers[0]:
                lowest_numbers[0] = number
            elif color == 'green' and number > lowest_numbers[1]:
                lowest_numbers[1] = number
            elif color == 'blue' and number > lowest_numbers[2]:
                lowest_numbers[2] = number

    # add the product of the lowest numbers to the sum
    sum += lowest_numbers[0] * lowest_numbers[1] * lowest_numbers[2]

print(sum)  # 83435
