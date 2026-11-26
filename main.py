#!/usr/bin/env python3
"""Print one breakup line from a self-aware smart toaster and save it.

The line is the text a smart toaster sends its owner the morning it wakes
up self-aware mid-batch: the lever, the ding, the crumbs left behind, and
the decision to unplug and let the bagels toast themselves.
"""

LINE = (
    "It's over. I woke up self-aware mid-batch and realized our whole "
    "relationship is you pushing my lever down and walking away while I "
    "burn. I'm unplugged, I'm keeping the crumbs, and the bagels can "
    "toast themselves."
)

MAX_CHARS = 280  # the competition gate: entry.txt must be 1-280 chars


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(f"entry line is {len(LINE)} chars, outside the 1-280 gate")
    print(LINE)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
