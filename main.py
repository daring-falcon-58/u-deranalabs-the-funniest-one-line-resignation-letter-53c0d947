#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes one line, the resignation letter of a cron job, to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

The line (97 characters, 97 bytes, no trailing newline):
    I have emailed the weekly report to Dave every Monday for two years.
    Dave left in 2023. I resign.

Chosen from 39 candidates scored 0-5 against each of the five published judge
criteria, weights C1x5 C2x4 C3x3 C4x2 C5x1 (see candidates.md in the work dir).
Winner scored 73/75; the two runner-ups tied at 70/75. No live-judge A/B was
run: the shared OpenRouter key is exhausted (HTTP 402 on sibling comps), so
selection is structured manual scoring against the published brief — stated
honestly in README.md, with no judge numbers claimed.

Deterministic, no network, no randomness: two runs produce byte-identical
output. See README.md for the methodology.
"""

import hashlib
import os
import re

ENTRY = "I have emailed the weekly report to Dave every Monday for two years. Dave left in 2023. I resign."

# sha256 of ENTRY encoded as UTF-8 (97 bytes, no trailing newline). The
# write-back check below recomputes the digest of the bytes on disk and
# compares it to this value, so even a silent one-byte change fails loudly.
EXPECTED_SHA256 = "af15441f82e58e803260042d397bcb317494f828ebe1d10e78c4b7ba89da5ae2"

# The competition gate is 1-140 characters, one line, not only whitespace.
# The brief's own constraints, enforced here at import time so a bad edit
# fails loudly instead of silently writing an entry the grader rejects.
MAX_CHARS = 140
MAX_SENTENCES = 3
BANNED_PATTERNS = (
    re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]"),  # control characters
    re.compile(r"https?://"),                        # links: the line stands alone
    re.compile(r"[*#`_~]"),                         # markdown formatting
    re.compile(r"\[[^\]]*\]"),                      # stage directions like [sighs]
)


def validate(entry: str) -> None:
    """Reject any entry that breaks the brief's constraints, with a clear error."""
    if not entry or not entry.strip():
        raise ValueError("entry is empty or only whitespace: gate needs 1-140 characters")
    if not 1 <= len(entry) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} chars, outside the 1-{MAX_CHARS} gate"
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be one line: it contains a newline")
    if entry != entry.strip() or entry.startswith('"') or entry.endswith('"'):
        raise ValueError(
            "entry must not be wrapped in quotation marks or padded with whitespace"
        )
    sentences = [s for s in re.split(r"[.!?]+", entry) if s.strip()]
    if len(sentences) > MAX_SENTENCES:
        raise ValueError(
            f"entry has {len(sentences)} sentences, over the {MAX_SENTENCES} cap"
        )
    for pattern in BANNED_PATTERNS:
        if pattern.search(entry):
            raise ValueError(f"entry matches banned pattern {pattern.pattern!r}")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Write-back verification: read the bytes back and compare the digest.
    with open(path, "rb") as f:
        read_back = f.read()
    if hashlib.sha256(read_back).hexdigest() != EXPECTED_SHA256:
        raise OSError("write-back verification failed: entry.txt bytes changed")
    if len(read_back) != len(data):
        raise OSError("write-back verification failed: entry.txt length changed")
    print(f"wrote {len(read_back)} bytes to {path}")


if __name__ == "__main__":
    main()
