"""One-line entry for the make.fun 'Make the Judge Smile' bounty.

Writes a single line (under 200 characters) about a small good thing
that happened today to /output/entry.txt.
"""

import os

LINE = "This morning the neighbour's cat stole my left sandal, then dragged it back to my doorstep like an apology — and that tiny apology made my whole day."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
