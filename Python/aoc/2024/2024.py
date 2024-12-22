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
    "dec5/1.py": "6612",
    "dec5/2.py": "4944",
    "dec6/1.py": "4789",
    "dec6/2.py": "1304",
    "dec7/1.py": "28730327770375",
    "dec7/2.py": "424977609625985",
    "dec8/1.py": "379",
    "dec8/2.py": "1339",
    "dec9/1.py": "6331212425418",
    "dec9/2.py": "6363268339304",
    "dec10/1.py": "552",
    "dec10/2.py": "1225",
    "dec11/1.py": "202019",
    "dec11/2.py": "239321955280205",
    "dec12/1.py": "1361494",
    "dec12/2.py": "830516",
    "dec13/1.py": "31552",
    "dec13/2.py": "95273925552482",
    "dec14/1.py": "231019008",
    "dec14/2.py": "8280",
    "dec15/1.py": "1415498",
    "dec15/2.py": "1432898",
    "dec16/1.py": "94436",
    "dec16/2.py": "481",
    "dec17/1.py": "3,1,4,3,1,7,1,6,3",
    "dec17/2.py": "37221270076916",
    "dec18/1.py": "294",
    "dec18/2.py": "31,22",
    "dec19/1.py": "251",
    "dec19/2.py": "616957151871345",
    "dec20/1.py": "1365",
    "dec20/2.py": "986082",
    "dec21/1.py": "107934",
    "dec21/2.py": "130470079151124",
    "dec22/1.py": "12979353889",
    "dec22/2.py": "1449",
}


def spinner(stop_event):
    while not stop_event.is_set():
        for frame in "|/-\\":
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

to_skip = [
    "dec7/2.py",
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