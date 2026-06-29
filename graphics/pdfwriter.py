from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

PAGE_WIDTH = 55 * mm
PAGE_HEIGHT = 6.4 * mm


def draw_pattern(filename, pattern):

    c = canvas.Canvas(filename, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

    module = 0.33 * mm      # ühe mooduli laius
    x = 2 * mm              # quiet zone

    for bit in pattern:

        if bit == "1":
            c.rect(
                x,
                0,
                module,
                PAGE_HEIGHT,
                fill=1,
                stroke=0
            )

        x += module

    c.save()