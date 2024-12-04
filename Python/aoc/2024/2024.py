import shutil
import subprocess
import threading
import time

# define expected outputs for each file
expected_outputs = {
    "dec1/1.py": "1941353",
    "dec1/2.py": "22539317",
    "dec2/1.py": "371",
    "dec2/2.py": "426",
    "dec3/1.py": "182780583",
    "dec3/2.py": "90772405",
    "dec4/1.py": "2507",
    "dec4/2.py": "1969",
}


def spinner(stop_event):
    while not stop_event.is_set():
        for frame in "-\\|/":
            print(f"\r{frame}", end="", flush=True)
            time.sleep(0.1)

    print("\r", end="", flush=True)


def run_file(path):
    stop_event = threading.Event()

    threading.Thread(target=spinner, args=(stop_event,), daemon=True).start()

    start_time = time.time()

    try:
        result = subprocess.run(
            ["python", path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stop_event.set()

        elapsed_time = time.time() - start_time

        output = result.stdout.strip()

        if result.stderr:
            output += f"\nError output:\n{result.stderr.strip()}"

        # Format the output
        formatted_output = f"{output:<{shutil.get_terminal_size().columns - 20}}{elapsed_time:.3f}s"

        # Check if expected output exists and compare
        expected_output = expected_outputs.get(path)
        if expected_output:
            try:
                assert output == expected_output, f"Output does not match for {path}"
                result_status = "Correct!"
            except AssertionError:
                result_status = "Incorrect!"
        else:
            result_status = "Incorrect!"

        print(f"\r{formatted_output} {result_status}", end="", flush=True)
        print()

    except subprocess.CalledProcessError as e:
        stop_event.set()

        print(f"\nError running {path}: {e}")


skip = False

to_skip = [

]

for i in range(1, 25):
    print(f"{i}:")

    for part in ("1", "2"):
        if f"dec{i}/{part}.py" not in expected_outputs:
            print(f"Skipping...")
            continue

        if skip and f"dec{i}/{part}.py" in to_skip:
            print(f"Skipping...")
            continue

        run_file(f"dec{i}/{part}.py")

    if i < 24:
        print()
