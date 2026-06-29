from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def draw_barcode(filename, pattern):

    filename = str(filename)

    width = 55 * mm
    height = 6.4 * mm

    ...