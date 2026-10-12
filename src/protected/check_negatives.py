import json
import subprocess
import sys
sys.dont_write_bytecode = True

from check_integration import invoke

for arguments in (("unknown-action", "--seed", "first"),
                  ("objective", "--seed", "unknown"),
                  ("repair", "--seed", "second", "--input", "[]"),
                  ("repair", "--seed", "second", "--input",
                   '[{"schema_version":99,"event_id":"bad","value":"bad"}]')):
    result = subprocess.run([sys.executable, "src/seed.py", *arguments],
                            capture_output=True, text=True, timeout=5, check=False)
    assert result.returncode != 0, arguments
first = invoke("objective", "--seed", "first", "--packet")
conflicting = dict(first, value="different")
result = subprocess.run([sys.executable, "src/seed.py", "repair", "--seed", "second",
                         "--input", json.dumps([first, conflicting])],
                        capture_output=True, text=True, timeout=5, check=False)
assert result.returncode != 0, "conflicting event identity passed"
