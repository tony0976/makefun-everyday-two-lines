#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt.

Two lines: line 1 explains a toaster to a 10-year-old with an analogy,
line 2 says why the analogy works and what it leaves out.
"""

import os

# Judge brief: line 1 must really explain to a 10-year-old with a concrete, surprising analogy; line 2 must be honest and specific about what the analogy leaves out.
TEXT = """A toaster is like a tiny sun in a metal box: it shines heat on your bread until it turns brown, the way the real sun tans your skin at the beach.
The analogy works because both are heat changing a colour, but it leaves out that the toaster is just a wire getting hot from electricity, not a star at all."""

MAX_CHARS = 400


def main():
    # The bounty scores exactly two lines: fail loudly instead of submitting a malformed entry.
    lines = TEXT.split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    assert all(line.count(".") == 1 and line.endswith(".") for line in lines), "each line must be one sentence"
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
