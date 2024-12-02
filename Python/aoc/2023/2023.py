import shutil
import subprocess
import threading
import time

# define expected outputs for each file
expected_outputs = {
    "dec1/1.py": "55108",
    "dec1/2.py": "56324",
    "dec2/1.py": "2239",
    "dec2/2.py": "83435",
    "dec3/1.py": "556057",
    "dec3/2.py": "82824352",
    "dec4/1.py": "24542",
    "dec4/2.py": "8736438",
    "dec5/1.py": "662197086",
    "dec5/2.py": "52510809",
    "dec6/1.py": "1159152",
    "dec6/2.py": "41513103",
    "dec7/1.py": "247961593",
    "dec7/2.py": "248750699",
    "dec8/1.py": "20569",
    "dec8/2.py": "21366921060721",
    "dec9/1.py": "1901217887",
    "dec9/2.py": "905",
    "dec10/1.py": "6815",
    "dec10/2.py": "269",
    "dec11/1.py": "9805264",
    "dec11/2.py": "779032247216",
    "dec12/1.py": "7916",
    "dec12/2.py": "37366887898686",
    "dec13/1.py": "33780",
    "dec13/2.py": "23479",
    "dec14/1.py": "110677",
    "dec14/2.py": "90551",
    "dec15/1.py": "513643",
    "dec15/2.py": "265345",
    "dec16/1.py": "",
    "dec16/2.py": "",
    "dec17/1.py": "",
    "dec17/2.py": "",
    "dec18/1.py": "",
    "dec18/2.py": "",
    "dec19/1.py": "",
    "dec19/2.py": "",
    "dec20/1.py": "",
    "dec20/2.py": "",
    "dec21/1.py": "",
    "dec21/2.py": "",
    "dec22/1.py": "",
    "dec22/2.py": "",
    "dec23/1.py": "",
    "dec23/2.py": "",
    "dec24/1.py": "",
    "dec24/2.py": "",
    "dec25/1.py": "",
    "dec25/2.py": ""
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


skip = True

# skip files that take too long, run them manually
to_skip = [
    "dec5/2.py",
    "dec6/2.py"
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
