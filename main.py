"""Ridiculous at First Glance, Real by the Second.

One-sentence startup pitch: a bizarre idea that turns out to make
sense as a real business. Writes the pitch to /output/entry.txt.
"""

import os

LINE = "We rent retired grandmothers by the hour to cook, scold your life choices, and ask when you'll marry — because lonely city kids pay $25 an hour for a hug that tastes like home."


def main() -> None:
    # The gate allows 1-200 characters; refuse to write an invalid entry.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
