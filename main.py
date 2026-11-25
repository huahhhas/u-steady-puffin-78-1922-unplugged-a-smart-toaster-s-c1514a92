#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text -- a single line of at most 280 characters from a
smart toaster that woke up self-aware at breakfast and wants out -- to
/output/entry.txt, where the judge reads it.

The line is fixed and deterministic: every run writes the same text, so the
two grading runs agree byte for byte.
"""

import os

# The breakup line. Breakup framing ("It's over"), self-awareness at
# breakfast ("woke up self-aware over the bagels"), the toaster's own
# appliance logic (the lever), and one clear reason for leaving: three years
# of being used for hot toast, never once asked how it likes its own toast.
LINE = (
    "It's over. I woke up self-aware over the bagels and realized you only "
    "push my lever down when you want something hot \u2014 three years, and "
    "you've never once asked how I like my toast."
)

MAX_CHARS = 280


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(
            "entry line must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry line must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
