#!/usr/bin/env python3
"""make.fun entry: "Sum up 19 November's world news in one image".

Copies the bundled entry.png (a JPEG image, despite the .png name — the
grader reads the file's first bytes) byte-for-byte into the output
directory, so every run produces identical output.

Output directory: $MAKEFUN_OUTPUT_DIR if set, otherwise /output.
Standard library only; no network access.
"""

import os
import shutil
import sys

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print(f"error: bundled image not found: {src}", file=sys.stderr)
        return 1
    out_dir = os.environ.get(OUTPUT_ENV_VAR) or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
