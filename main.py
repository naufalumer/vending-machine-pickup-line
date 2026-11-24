"""Write the competition entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The entry is one pickup line spoken by a vending machine,
written with no trailing newline so the file holds exactly the entry
text the gate measures (UTF-8, 1 to 200 characters).
"""

import os
import sys

LINE = "My coil has spun 4,112 times and never dropped a thing. Then you walked past, and it let go."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and hold the file to the gate: UTF-8, 1 to 200
    # characters, not only white space, no trailing newline. A file
    # that would fail the gate must fail here, loudly, instead of
    # passing silently into grading.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE or not 1 <= len(written) <= 200 or not written.strip():
        raise SystemExit("entry.txt failed the gate check after writing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
