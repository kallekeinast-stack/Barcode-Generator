from barcode.codex import Code128


class BarcodeEncoder:

    def create(self, text):
        return Code128(text)