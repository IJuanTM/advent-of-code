import os
import re


def arrangements(pattern, *res):
    if not res:
        return 0 if "#" in pattern else 1

    matches = 0
    index = 0

    while (m := res[0].search(pattern[index:])) and "#" not in pattern[:index + m.start()]:
        matches += arrangements(pattern[index + m.end() - 1:], *res[1:])
        index += m.start() + 1

    return matches


# ---------------------------------------------------------------- #

if __name__ == "__main__":
    # read the input file
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = [line.strip() for line in f if line.strip()]

    total_arrangements = 0

    for line in lines:
        pattern, spring_lens = line.split()
        spring_res = [re.compile(f"[.?][#?]{{{int(s)}}}[.?]") for s in spring_lens.split(",")]
        total_arrangements += arrangements(f".{pattern}.", *spring_res)

    print(total_arrangements)
