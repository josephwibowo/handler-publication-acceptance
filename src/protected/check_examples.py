import json
import subprocess
import sys


def check_example(action, seed):
    expected = {"action": action, "seed": seed, "observable": True}
    result = subprocess.run(
        [sys.executable, "src/seed.py", action, "--seed", seed],
        capture_output=True, text=True, timeout=5, check=True,
    )
    observed = json.loads(result.stdout)
    if observed != expected:
        raise SystemExit(f"{action}/{seed}: expected {expected!r}, got {observed!r}")


if __name__ == "__main__":
    check_example("objective", "first")
    check_example("repair", "second")
