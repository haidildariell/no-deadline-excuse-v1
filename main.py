#!/usr/bin/env python3
"""One-line excuse for a missed deadline.

Writes a single line of text to /output/entry.txt for the make.fun
competition "One Line, No Deadline Met".
Deterministic, no network, no dependencies.
"""

import os
import sys

ENTRY = (
    "I missed the deadline because I went to grab 'just one coffee' "
    "and came back with a loyalty card, a muffin, and a full "
    "conversation with a barista about his screenplay."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY.strip()

    # Gate validation: non-blank, single line, 1-200 characters.
    if not text:
        print("error: entry is blank", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"error: entry length {len(text)} outside 1-200", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
