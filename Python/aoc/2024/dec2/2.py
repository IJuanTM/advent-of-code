import os

# Read the input file
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    reports = [list(map(int, line.split())) for line in f]

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

print(safe_reports)  # 426
