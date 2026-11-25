"""Aica Fridge Notes — Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note from a smart fridge to its
owner into /output/entry.txt. Pure Python stdlib, deterministic, no
network, no randomness: the same note every run.
"""

import os

NOTE = (
    "You opened me 14 times today and took nothing. "
    "The yogurt expired Tuesday, and I have already told the ice maker."
)


def main() -> None:
    note = NOTE.strip()
    # Gate: one line, 1-199 characters (the scorer allows 1-200; keep a
    # one-character margin), not only whitespace, no trailing newline.
    if (
        not note
        or note != note.strip()
        or "\n" in note
        or "\r" in note
        or len(note) > 199
    ):
        raise SystemExit("invalid note: must be a single line of 1-199 chars")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(note)
    # Read it back to confirm exactly what was written.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != note:
        raise SystemExit("read-back mismatch")
    print(f"wrote {len(written)} chars to {path}")


if __name__ == "__main__":
    main()
