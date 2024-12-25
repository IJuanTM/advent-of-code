import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [l.split() for l in f if '->' in l]

r = lambda c, y: any(y == x and c in (a, b) for a, x, b, _, _ in lines)

print(*sorted(c for a, x, b, _, c in lines if
              x == "XOR" and all(d[0] not in 'xyz' for d in (a, b, c)) or
              x == "AND" and not "x00" in (a, b) and r(c, 'XOR') or
              x == "XOR" and not "x00" in (a, b) and r(c, 'OR') or
              x != "XOR" and c[0] == 'z' and c != "z45"), sep=',')  # bmn,jss,mvb,rds,wss,z08,z18,z23