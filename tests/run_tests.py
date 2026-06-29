from tests.test_checksum import test_checksum


try:

    test_checksum()

    print("Kõik testid läbisid.")

except AssertionError:

    print("TEST EBAÕNNESTUS!")