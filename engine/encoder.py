from barcode import Code128


class BarcodeEncoder:

    def __init__(self):
        pass

    def create(self, text):

        barcode = Code128(text)

        return barcode