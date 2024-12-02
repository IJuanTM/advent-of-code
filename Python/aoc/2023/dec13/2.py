import os

# read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    patterns = [l.splitlines() for l in f.read().split('\n\n')]


# ---------------------------------------------------------------- #


def mirror(pat, p):
    for i in range(1, len(pat[0])):
        if sum(sum(x != y for x, y in zip(l[:i][::-1], l[i:])) for l in pat) == p:
            return i
    return 0


# output the result
print(sum(mirror(pat, 1) + 100 * mirror(list(zip(*pat)), 1) for pat in patterns))
