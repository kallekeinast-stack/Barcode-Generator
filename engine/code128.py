"""
Code128 Encoder
Version 1.0
Only Code Set B
"""

START_B = 104
STOP = 106


def encode_char(ch):
    """
    Tagastab Code128B sümboli väärtuse.

    ASCII 32 = 0
    ASCII 33 = 1
    ...
    ASCII 126 = 94
    """

    value = ord(ch)

    if value < 32 or value > 126:
        raise ValueError(f"Unsupported character: {ch}")

    return value - 32


def encode_text(text):
    """
    Muudab teksti Code128 väärtusteks.

    Näiteks

    HELLO

    ↓

    [40,37,44,44,47]
    """

    values = []

    for ch in text:
        values.append(encode_char(ch))

    return values