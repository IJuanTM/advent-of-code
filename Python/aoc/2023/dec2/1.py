import os

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    games = f.read().splitlines()

# ---------------------------------------------------------------- #

sum = 0

for game in games:
    valid = True

    # get the game number and the game
    game_number, game = map(str.strip, game.split(':'))

    for set in [set.strip() for set in game.split(';')]:
        red, green, blue = 0, 0, 0

        for cube in [cube.strip() for cube in set.split(',')]:
            # get the number and color of the cube
            number, color = map(str.strip, cube.split(' '))

            # add the number to the color depending on the color
            if color == 'red':
                red += int(number)
            elif color == 'green':
                green += int(number)
            elif color == 'blue':
                blue += int(number)

        # if the red number is greater than 12, the green number is greater than 13, or the blue number is greater than 14, the game is invalid
        if red > 12 or green > 13 or blue > 14:
            valid = False
            break

    # if the game is invalid, continue
    if not valid:
        continue

    # add the game number to the sum
    sum += int(game_number.split(' ')[1])

print(sum)  # 2239
