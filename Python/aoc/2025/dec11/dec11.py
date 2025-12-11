def part_1():
    graph = {}
    for line in lines:
        device, outputs = line.split(': ')
        graph[device] = outputs.split()

    memo = {}

    def count_paths(current):
        if current == 'out':
            return 1
        if current not in graph:
            return 0
        if current in memo:
            return memo[current]

        total = sum(count_paths(next_device) for next_device in graph[current])
        memo[current] = total
        return total

    return count_paths('you')


def part_2():
    graph = {}
    for line in lines:
        device, outputs = line.split(': ')
        graph[device] = outputs.split()

    memo = {}

    def count_paths(current, visited_required):
        if current == 'out':
            return 1 if visited_required == ('dac', 'fft') else 0
        if current not in graph:
            return 0

        state = (current, visited_required)
        if state in memo:
            return memo[state]

        new_visited = visited_required
        if current in ('dac', 'fft') and current not in visited_required:
            new_visited = tuple(sorted(visited_required + (current,)))

        total = sum(count_paths(next_device, new_visited) for next_device in graph[current])
        memo[state] = total
        return total

    return count_paths('svr', ())


if __name__ == "__main__":
    import os

    EXPECTED = (506, 385912350172800)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = [line.strip() for line in f]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
