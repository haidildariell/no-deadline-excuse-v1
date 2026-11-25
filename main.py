#!/usr/bin/env python3
"""One-liner entry: One Line, No Deadline Met.

Writes the winning one-liner to /output/entry.txt.
Deterministic, no network, no dependencies.
"""

ENTRY_PARTS = (
    "I missed the deadline because I went to grab 'just one coffee' ",
    "and came back with a loyalty card, a muffin, and a full ",
    "conversation with a barista about his screenplay.",
)


def build_entry_text() -> str:
    """Assemble the entry text from its parts."""
    return "".join(ENTRY_PARTS)


def validate_entry(text: str) -> None:
    """Check the entry against the competition gate.

    The gate requires 1-200 characters, a single line, and
    non-blank content.
    """
    if not text.strip():
        raise ValueError("entry text must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry text must be 1-200 characters")


def main() -> None:
    text = build_entry_text()
    validate_entry(text)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
