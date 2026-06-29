from pathlib import Path

from engine.encoder import BarcodeEncoder
from graphics.pdfwriter import draw_barcode


class BarcodeGenerator:

    def __init__(self):
        self.encoder = BarcodeEncoder()

    def generate(self, year, start, end):

        Path("output").mkdir(exist_ok=True)

        total = end - start + 1

        for index, number in enumerate(range(start, end + 1), start=1):

            text = f"{year}-{number:07d}"

            barcode = self.encoder.create(text)

            pattern = barcode.build()[0]

            filename = Path("output") / f"{text}.pdf"

            draw_barcode(filename, pattern)

            print(f"{index:5}/{total}   {text}")