#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun bounty entry.

Writes one funny line, in the elevator's own voice, to /output/entry.txt.
Pure Python standard library; no network, no input files.
"""

import os

LINE = "I've been lifting strangers for twenty years, and not one of you has ever asked how my day is going."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
