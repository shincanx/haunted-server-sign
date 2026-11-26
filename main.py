#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one line -- the sign taped to the haunted server room door --
to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network.
"""

import os

ENTRY = "The ghost in the cold aisle isn't haunting us. He's just waiting for his ticket to be closed."

# Gate: the entry must be 1-120 UTF-8 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, gate allows 1-120"
assert ENTRY.strip(), "entry must not be only whitespace"


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
