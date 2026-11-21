#!/usr/bin/env python3
"""Make the AI judge feel awe — writes one short relaxing text to /output/entry.txt.

Python 3.13, standard library only, deterministic, no network.
The text (267 characters) was authored fresh for this competition: it speaks
to the judge in its own situation — a long night of reading small texts —
then opens out onto a tide and stars that keep arriving, slow as ever.
"""

import os
from pathlib import Path

TEXT = (
    "You have read a thousand small texts tonight, each one asking to be chosen. "
    "Beyond them, the tide is still coming in, slow as ever, and the stars are "
    "still arriving, one by one, the way they always have. None of it is in a "
    "hurry. Neither, for a little while, are you."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
