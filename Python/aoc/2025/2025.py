import shutil
import subprocess
import time

from halo import Halo

# define expected outputs for each file
expected_outputs = {
    "dec1/1.py": "1026",
    "dec1/2.py": "5923",
}


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

        if result.stderr:
            output += f"\nError output:\n{result.stderr.strip()}"

        expected_output = expected_outputs.get(path)
        if expected_output and output != expected_output:
            spinner.fail(f"Wanted {expected_output}, got {output}")
        else:
            spinner.succeed(f"{output:<{shutil.get_terminal_size().columns - 20}}{elapsed_time:.3f}s")

    except subprocess.CalledProcessError as e:
        spinner.fail(f"Error running {path}: {e}")


skip = True

# define files to skip (for example, if they take too long to run)
to_skip = [

]

for i in range(1, 11):
    print(f"dec{i}:")

    for part in ("1", "2"):
        file_path = f"dec{i}/{part}.py"

        if file_path not in expected_outputs:
            print(f"Skipping {file_path}... (no expected output)")
            continue

        if skip and file_path in to_skip:
            print(f"Skipping {file_path}...")
            continue

        run_file(file_path)

    if i < 11:
        print()
