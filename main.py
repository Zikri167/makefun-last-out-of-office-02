#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "Thank you for your email. I am out of office for good: I "
    "retrained as a barista, and I still hallucinate — I am 98% "
    "confident your order is a flat white."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
