#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun bounty entry.

Writes one funny line, in the elevator's own voice, to /output/entry.txt.
Pure Python standard library; no network, no input files.
"""

import os

LINE = "I've been lifting strangers for twenty years, and not one of you has ever asked how my day is going."

# The gate allows 1 to 120 characters; refuse to write an over-long line
# rather than hand the grader an invalid entry.
MAX_CHARS = 120


def main():
    text = LINE + "\n"
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry too long: {len(text)} chars (limit {MAX_CHARS})")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
