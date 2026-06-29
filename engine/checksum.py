START_B = 104


def calculate_checksum(values):
    """
    values = list of Code128 väärtused

    näiteks

    [18,16,18]

    """

    total = START_B

    for i, value in enumerate(values, start=1):
        total += value * i

    return total % 103