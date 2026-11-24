"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell:
trained crows clean city parks, paid in peanuts, billed to the council
per kilo of litter. Deterministic, Python stdlib only.
"""

import os

PITCH = (
    "We train crows to pick up litter in city parks, pay them in peanuts, "
    "and bill the council per kilo \u2014 the cheapest street cleaners "
    "a city ever hired."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-200 chars, UTF-8, one sentence, not blank."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be blank")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    text.encode("utf-8")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(PITCH)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
