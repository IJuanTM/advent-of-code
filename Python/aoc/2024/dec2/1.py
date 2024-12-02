import os

# Read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    reports = [list(map(int, line.split())) for line in f]

safe_reports = 0

for report in reports:
    differences = [b - a for a, b in zip(report, report[1:])]

    # Check if all differences are within the range [1, 3] or [-3, -1]
    valid_differences = all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences)

    # Check if all differences are either positive (increasing) or negative (decreasing)
    consistent_trend = all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)

    if valid_differences and consistent_trend:
        safe_reports += 1

print(safe_reports)  # 371
