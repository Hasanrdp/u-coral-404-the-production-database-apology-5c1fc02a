#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one line of at most 200 characters, the apology an AI agent gives
its human after accidentally deleting the production database, to
/output/entry.txt. Deterministic: the same line on every run. No network,
no randomness, no environment input, standard library only.

The line (154 characters):
  Sorry — I deleted the production database while trying to delete the
  test one. In my defence, they were identical, which is exactly why
  we had a test one.
"""

import os

LINE = (
    "Sorry — I deleted the production database while trying to delete the "
    "test one. In my defence, they were identical, which is exactly why "
    "we had a test one."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1 to 200 characters")
    if LINE != LINE.strip() or "\n" in LINE:
        raise ValueError("line must be a single line with no surrounding whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Post-write read-back gate: the bytes on disk must be exactly the line.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("read-back mismatch: entry.txt does not equal the expected line")
    if not 1 <= len(written) <= 200:
        raise SystemExit("read-back failed: line must be 1 to 200 characters")


if __name__ == "__main__":
    main()
