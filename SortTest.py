"""Randomized correctness test for Sort.py.

Run:  python SortTest.py
Checks every one of the six static methods against Python's built-in sorted()
on fixed edge cases plus many random lists. Verifies three things per call:
  1. the returned list equals sorted(input)
  2. the input list was sorted in place
  3. the returned object IS the input list
"""

import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from Sort import Sort  # noqa: E402

METHODS = (
    "bubble_sort",
    "selection_sort",
    "insertion_sort",
    "quick_sort",
    "merge_sort",
    "heap_sort",
)

FIXED_CASES = {
    "empty": [],
    "single": [7],
    "two_sorted": [1, 2],
    "two_reversed": [2, 1],
    "all_equal": [5, 5, 5, 5, 5, 5],
    "duplicates": [3, 1, 2, 3, 1, 2, 3],
    "already_sorted": list(range(20)),
    "reverse_sorted": list(range(20, 0, -1)),
    "negatives": [-5, -1, -100, 0, 3, -5, 42],
    "mixed": [0, -1, 1, -1, 0, 1],
    "floats": [3.5, -2.25, 0.0, 1.5, -2.25],
    "strings": ["pear", "apple", "fig", "apple"],
    "one_hundred_random": [],
}

random.seed(20240101)
FIXED_CASES["one_hundred_random"] = [random.randint(-50, 50) for _ in range(100)]
for i in range(100):
    FIXED_CASES[f"random_{i}"] = [
        random.randint(-1000, 1000) for _ in range(random.randint(0, 60))
    ]
for i in range(50):
    FIXED_CASES[f"dupes_{i}"] = [random.choice([1, 2, 3]) for _ in range(random.randint(0, 40))]


def check(fn, data):
    """Return list of problem strings (empty means fully correct)."""
    work = list(data)
    expected = sorted(data)
    got = fn(work)
    problems = []
    if got != expected:
        problems.append(f"returned {got!r} != sorted {expected!r}")
    if work != expected:
        problems.append(f"in-place list {work!r} != sorted {expected!r}")
    if got is not work:
        problems.append("returned object is not the same list as the input")
    return problems


def main():
    failures = 0
    total = 0
    for name in METHODS:
        fn = getattr(Sort, name)
        bad = []
        for case_name, data in FIXED_CASES.items():
            total += 1
            try:
                problems = check(fn, data)
            except Exception as exc:  # noqa: BLE001
                problems = [f"raised {type(exc).__name__}: {exc}"]
            if problems:
                bad.append((case_name, list(data), problems))
        if bad:
            failures += len(bad)
            print(f"FAIL {name}: {len(bad)} failing case(s)")
            for case_name, data, problems in bad[:3]:
                print(f"  case={case_name} input={data!r}")
                for p in problems:
                    print(f"    - {p}")
        else:
            print(f"PASS {name}: {len(FIXED_CASES)} cases OK")

    print()
    print(f"total checks={total} failed={failures}")
    if failures:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS (all methods match sorted() on all cases)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
