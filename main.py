#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge: write one note to /output/entry.txt.

The line: the fridge has watched the March leftovers breed in the back
and, petty as ever, named the eldest after its owner. Fridge voice throughout:
inventory-obsessed, smug about what it witnessed, grudge kept small and domestic.
Concrete detail (leftovers from March) + twist (named the eldest after you).
"""
import os

ENTRY = "The leftovers from March have started a family in the back. I named the eldest after you."

def main():
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY.strip() and ENTRY.strip()
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")

if __name__ == "__main__":
    main()
