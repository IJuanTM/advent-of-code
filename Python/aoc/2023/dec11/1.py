import os


def dist(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


def exdist(g1, g2, exrows, excols, exnum=2):
    x1, y1 = min(g1[0], g2[0]), min(g1[1], g2[1])
    x2, y2 = max(g1[0], g2[0]), max(g1[1], g2[1])

    res = dist(g1, g2)
    extra = sum(1 for r in exrows if x1 < r < x2) * (exnum - 1) + sum(1 for c in excols if y1 < c < y2) * (exnum - 1)
    return res + extra


def parse(image):
    galaxies, rows, cols = [], [], list(range(len(image[0])))
    for r, line in enumerate(image):
        if all(el == "." for el in line):
            rows.append(r)
        else:
            for c, el in enumerate(line):
                if el != ".":
                    cols = [col for col in cols if col != c]
                    galaxies.append((r, c))
    return galaxies, rows, cols


# ---------------------------------------------------------------- #

if __name__ == "__main__":
    # read the input file
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        image = [line.strip() for line in f if line.strip()]

    galaxies, rows, cols = parse(image)

    print(sum(exdist(galaxies[g1], galaxies[g2], rows, cols) for g1 in range(len(galaxies) - 1) for g2 in range(g1 + 1, len(galaxies))))  # 9805264
