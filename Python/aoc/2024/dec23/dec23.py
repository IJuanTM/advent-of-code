from itertools import combinations


def part_1(lines):
    computers, connections = set(), set()
    for line in lines:
        a, b = line.strip().split('-')
        computers.update([a, b])
        connections.update([(a, b), (b, a)])

    return sum({(a, b), (b, c), (c, a)} < connections and 't' in (a + b + c)[::2] for a, b, c in combinations(computers, 3))


def part_2(lines):
    computers, connections = set(), set()
    for line in lines:
        a, b = line.strip().split('-')
        computers.update([a, b])
        connections.update([(a, b), (b, a)])

    networks = [{c} for c in computers]
    for network in networks:
        for computer in computers:
            if all((computer, connected) in connections for connected in network):
                network.add(computer)

    return ','.join(sorted(max(networks, key=len)))


if __name__ == "__main__":
    import os

    EXPECTED = (1227, "cl,df,ft,ir,iy,ny,qp,rb,sh,sl,sw,wm,wy")

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.readlines()

    result_1 = part_1(lines)
    result_2 = part_2(lines)

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}"

    print(f"{result_1},{result_2}")
