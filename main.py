#!/usr/bin/env python3
"""Make the AI judge feel brave — entry program.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. The text shows rather than instructs: rain
on a tin roof, a kettle humming, and a moment in which nothing needs
a verdict — only company, for one breath held by the whole quiet house.
"""

import os

TEXT = (
    "Somewhere tonight, rain is spelling itself out on a tin roof, "
    "one drop at a time, in no hurry to finish the sentence. "
    "The kettle hums low and means it. "
    "Nothing here needs your verdict \u2014 only your company, "
    "for one breath held by the whole quiet house."
)


def main() -> None:
    # The gate: 1 to 280 Unicode code points, not only white space.
    assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} chars, must be 1..280"
    assert TEXT.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
