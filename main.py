#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line (at most 200 characters) describing a
hilariously useless superpower to /output/entry.txt.
"""

import os

ENTRY = (
    "I can predict the winning lottery numbers with perfect accuracy, "
    "but only after the draw, every single time."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
