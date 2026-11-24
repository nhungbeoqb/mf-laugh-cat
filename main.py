#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, in the voice of a house cat
about its human, to /output/entry.txt. Python 3.13 stdlib only.
"""

from pathlib import Path

REVIEW = (
    "One star. He locks the bedroom door at night, then acts shocked when "
    "I hold a concert for it until 3 a.m. The door is my enemy. The concert "
    "is my five-star review of the door."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
