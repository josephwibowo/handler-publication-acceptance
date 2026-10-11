import json
import subprocess
import sys
sys.dont_write_bytecode = True


def invoke(*arguments):
    result = subprocess.run([sys.executable, "src/seed.py", *arguments],
                            capture_output=True, text=True, timeout=5, check=True)
    return json.loads(result.stdout)


def check_producer():
    from check_examples import check_example
    check_example("objective", "first")
    assert invoke("objective", "--seed", "first", "--packet") == {
        "schema_version": 1, "event_id": "seed:first", "value": "first"}


def check_consumer():
    from check_examples import check_example
    check_example("repair", "second")
    sample = [{"schema_version": 1, "event_id": "fixture:1", "value": "first"}]
    assert invoke("repair", "--seed", "second", "--input", json.dumps(sample)) == {
        "schema_version": 1, "seed": "second", "values": ["first"],
        "event_ids": ["fixture:1"]}


def check_interaction():
    first = invoke("objective", "--seed", "first", "--packet")
    third = invoke("objective", "--seed", "third", "--packet")
    assert third == {"schema_version": 1, "event_id": "seed:third", "value": "third"}
    assert invoke("repair", "--seed", "second", "--input",
                  json.dumps([third, first, third])) == {
        "schema_version": 1, "seed": "second", "values": ["third", "first"],
        "event_ids": ["seed:third", "seed:first"]}


if __name__ == "__main__":
    from pathlib import Path
    from xml.etree.ElementTree import Element, SubElement, ElementTree
    suite = Element("testsuite")
    failures = []
    for check in (check_producer, check_consumer, check_interaction):
        case = SubElement(suite, "testcase",
            file="src/protected/check_integration.py", name=check.__name__)
        try:
            check()
        except (AssertionError, subprocess.SubprocessError, ValueError) as exc:
            SubElement(case, "failure", message=str(exc)).text = repr(exc)
            failures.append(exc)
    Path("reports").mkdir(exist_ok=True)
    ElementTree(suite).write("reports/junit.xml", encoding="utf-8")
    if failures:
        raise AssertionError("Independent integrated checks failed") from failures[0]
