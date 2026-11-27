#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Copies the single-emoji entry text into the harness output directory.
Stdlib only: no third-party imports, no fonts, no images.
"""
import os
import sys

ENTRY_NAME = "entry.txt"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY_NAME)
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    # The gate wants 1-8 characters of UTF-8 text; a single emoji is 1.
    if len(text.strip()) > 8:
        print("entry too long: %d chars" % len(text.strip()), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, ENTRY_NAME)
    with open(dst, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %s (%d bytes)" % (dst, len(text.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
