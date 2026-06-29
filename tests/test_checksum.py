from barcode.checksum import calculate_checksum


def test_checksum():

    values = [18, 16, 18]

    result = calculate_checksum(values)

    assert result == 2