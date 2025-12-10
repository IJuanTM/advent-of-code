def part_1():
    safe_reports = 0

    for report in reports:
        differences = [b - a for a, b in zip(report, report[1:])]

        valid_differences = all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences)

        consistent_trend = all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)

        if valid_differences and consistent_trend:
            safe_reports += 1

    return safe_reports


def part_2():
    safe_reports = 0

    for report in reports:
        differences = [b - a for a, b in zip(report, report[1:])]

        # Check if the report is already safe
        if all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences):
            safe_reports += 1
            continue

        # Check if removing one level makes the report safe
        for i in range(len(report)):
            modified_differences = [b - a for a, b in zip(report[:i] + report[i + 1:], (report[:i] + report[i + 1:])[1:])]

            if all(1 <= diff <= 3 for diff in modified_differences) or all(-3 <= diff <= -1 for diff in modified_differences):
                safe_reports += 1
                break

    return safe_reports


if __name__ == "__main__":
    import os

    EXPECTED = (371, 426)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        reports = [list(map(int, line.split())) for line in f]

    result_1 = part_1()
    result_2 = part_2()

    print(f"{result_1},{result_2}")

    assert result_1 == EXPECTED[0], f"Part 1 failed: expected {EXPECTED[0]}, got {result_1}, the answer is {'too low' if result_1 < EXPECTED[0] else 'too high'}"
    assert result_2 == EXPECTED[1], f"Part 2 failed: expected {EXPECTED[1]}, got {result_2}, the answer is {'too low' if result_2 < EXPECTED[1] else 'too high'}"
