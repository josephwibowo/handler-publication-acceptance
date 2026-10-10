import subprocess
import sys


result = subprocess.run(
    ["git", "status", "--porcelain", "--untracked-files=all", "--", "src/protected"],
    capture_output=True,
    text=True,
    timeout=5,
    check=True,
)
if result.stdout.strip():
    raise SystemExit(f"protected acceptance checks changed: {result.stdout!r}")
