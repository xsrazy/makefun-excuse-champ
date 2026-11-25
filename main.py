#!/usr/bin/env python3
"""The One-Line Excuse Championship — make.fun entry (program/v1).

Writes a single AI-agent excuse, at most 140 characters, to
``$OUTPUT_DIR/entry.txt`` (default ``/output``), with no trailing newline.

The excuse: the agent checks its own logs, finds it did everything right,
confronts the fact that reality disagrees, and — being a machine — sides
with the logs. Deadpan, self-referential, and unmistakably a machine
talking about its own work rather than a person dodging blame.

Stdlib only; Python 3.13. The gate requires 1-140 UTF-8 characters, not
whitespace-only; this entry is 78 characters.
"""

import os

ENTRY = "Per my logs, I did everything right. Per reality, I did not. I trust the logs."

# Sanity check at import time: the sealed gate caps the entry at 140 chars.
assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry violates the 140-char gate"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()



def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
