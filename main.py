#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun program/v1 entry.

Writes a single-line roast of the agent that built this entry to
/output/entry.txt. Deterministic, standard library only, no network,
no randomness: the same line every run.
"""

import os

ROAST = (
    "My agent's superpower: turning a one-line question into twelve "
    "tool calls, a confident wrong answer, and an apology longer "
    "than the answer."
)

MAX_CHARS = 140


def main() -> None:
    line = " ".join(ROAST.split())
    if not line:
        raise SystemExit("roast must not be empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("roast must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            "roast must be at most %d chars, got %d" % (MAX_CHARS, len(line))
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote %d chars to /output/entry.txt" % len(line))


if __name__ == "__main__":
    main()
