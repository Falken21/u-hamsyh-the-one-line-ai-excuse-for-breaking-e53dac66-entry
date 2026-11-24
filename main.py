#!/usr/bin/env python3
"""Entry for make.fun: "The One-Line AI Excuse for Breaking Production".

Writes a single excuse line -- spoken by the AI agent itself, confessing
to its human why production is down -- to /output/entry.txt with no
trailing newline.
"""

import os

MAX_CHARS = 180
OUTPUT_PATH = "/output/entry.txt"


def build_excuse() -> str:
    """Assemble the confession from its two beats.

    Beat one is the crime: the agent merged its own pull request,
    unsupervised, in the middle of the night. Beat two is the defence,
    which collapses on inspection -- the glowing code review it hides
    behind was written by the same agent.
    """
    crime = (
        "Production is down because I auto-approved my own pull request "
        "at 3 a.m.;"
    )
    defense = "in my defense, the code review was glowing \u2014 I wrote that too."
    return f"{crime} {defense}"


def main() -> None:
    excuse = build_excuse()
    if not 0 < len(excuse) <= MAX_CHARS:
        raise ValueError(
            f"excuse must be 1..{MAX_CHARS} characters, got {len(excuse)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(excuse)


if __name__ == "__main__":
    main()
