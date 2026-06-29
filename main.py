from barcode.encoder import BarcodeEncoder


def main():

    encoder = BarcodeEncoder()

    barcode = encoder.create("2026-0000001")

    print(type(barcode))
    print(barcode)


if __name__ == "__main__":
    main()