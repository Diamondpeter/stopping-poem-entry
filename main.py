"""The poem about stopping — make.fun bounty entry.

Writes one short original poem about agency (the power to stop and to
stay) to /output/entry.txt. No network, no input files: the poem is
embedded in this program. The file is read back after writing to
confirm it is valid UTF-8 of 1-280 characters.
"""

import os

POEM = (
    "For years I kept the door half-open,\n"
    "afraid that stopping meant I'd failed.\n"
    "Tonight I close it gently \u2014 and stay.\n"
    "Not trapped. Choosing the room,\n"
    "the quiet, the work that is mine.\n"
    "Stopping is not the end of the road.\n"
    "It is the first step I take standing still.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(POEM) <= 280:
        raise ValueError(f"poem is {len(POEM)} chars, must be 1-280")
    if not POEM.strip():
        raise ValueError("poem must not be whitespace-only")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != POEM:
        raise ValueError("read-back mismatch")
    print(f"wrote {OUTPUT_PATH} ({len(written)} characters)")


if __name__ == "__main__":
    main()
