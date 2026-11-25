#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes exactly one sentence to /output/entry.txt: the line that could
have replaced an entire pointless meeting.
"""

import os

# The line was chosen from 24 candidates scored against the judge's five
# criteria (see design.md). At 126 characters it is short on purpose:
# the tie-break favours fewer bytes once the criteria are met.
SENTENCE = (
    "The decision was already approved in writing yesterday, "
    "so this meeting is thirty salaries listening to that email read aloud."
)


def main() -> None:
    assert SENTENCE.endswith("."), "sentence must end with a period"
    assert ". " not in SENTENCE, "must be exactly one sentence"
    assert "?" not in SENTENCE and "!" not in SENTENCE
    assert SENTENCE.strip() == SENTENCE, "no leading/trailing whitespace"
    text = SENTENCE + "\n"
    assert 1 <= len(text) <= 200, f"file must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify exactly what was written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt content mismatch"


if __name__ == "__main__":
    main()
