"""Write the single funniest excuse an AI agent could give its human
after missing a deadline.

The program writes exactly one line to ``entry.txt`` inside the output
directory given by the ``MAKEFUN_OUTPUT_DIR`` environment variable (or
``/output`` when the variable is not set). The file holds the line and
nothing else -- no trailing newline, no extra whitespace -- so the
stored bytes are the line itself and every run produces byte-identical
output. No network access, no files read outside this repository,
standard library only.

Why this excuse: an agent that misses a deadline because it got stuck
proving it is not a robot is funny precisely because the failure is
uniquely machine-shaped -- a human would never lose three hours to a
CAPTCHA, and the excuse is delivered completely straight-faced.
"""

import os

LINE = (
    "I was going to finish on time, but I got distracted by a CAPTCHA "
    "and spent three hours proving I was not a robot."
)

TERMINATORS = ".!?"


def validate(line: str) -> None:
    """Enforce the competition's rules for the excuse line."""
    if not line:
        raise ValueError("line must not be empty")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 200:
        raise ValueError("line must be at most 200 characters")
    marks = [c for c in line if c in TERMINATORS]
    if len(marks) != 1:
        raise ValueError("line must contain exactly one sentence terminator")
    if line[-1] not in TERMINATORS:
        raise ValueError("the sentence terminator must be the final character")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")  # the exact line, no trailing newline
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes to {path}")
    print(f"character count: {len(LINE)}")


if __name__ == "__main__":
    main()
