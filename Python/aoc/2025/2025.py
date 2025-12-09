import subprocess
import time
from pathlib import Path

from halo import Halo


def run_file(path):
    start_time = time.time()
    spinner = Halo(text=f'Running {path}', spinner='dots')
    spinner.start()

    try:
        result = subprocess.run(
            ["python", path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        elapsed_time = time.time() - start_time
        output = result.stdout.strip()

        parts = output.split(',')
        day_num = path.split('/')[0].replace('dec', '') if '/' in path else path.split('\\')[0].replace('dec', '')

        part1_str = f"Part 1: {parts[0]}" if len(parts) > 0 else ""
        part2_str = f"Part 2: {parts[1]}" if len(parts) > 1 else ""

        spinner.succeed(f"Dec {day_num:<8} {part1_str:<32} {part2_str:<32} {elapsed_time:.3f}s")

    except subprocess.CalledProcessError as e:
        elapsed_time = time.time() - start_time
        spinner.fail(f"{elapsed_time:.3f}s")
        if e.stderr:
            print(e.stderr.strip())


to_skip = []

dec_folders = sorted([d for d in Path('.').iterdir() if d.is_dir() and d.name.startswith('dec')], key=lambda x: int(x.name.replace('dec', '')))

for folder in dec_folders:
    file_path = folder / f"{folder.name}.py"

    if not file_path.exists():
        continue

    if str(file_path) in to_skip:
        print(f"Skipping {file_path}...")
        continue

    run_file(str(file_path))
