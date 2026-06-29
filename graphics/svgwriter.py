from xml.etree.ElementTree import Element, SubElement, ElementTree

MM_TO_PX = 3.779527559


def create_svg(filename, pattern,
               width_mm=55,
               height_mm=6.4,
               quiet_zone_mm=2):

    svg = Element(
        "svg",
        xmlns="http://www.w3.org/2000/svg",
        version="1.1",
        width=f"{width_mm}mm",
        height=f"{height_mm}mm",
        viewBox=f"0 0 {width_mm*MM_TO_PX} {height_mm*MM_TO_PX}"
    )

    module_count = len(pattern)

    usable_width = width_mm - quiet_zone_mm * 2

    module_width = usable_width / module_count

    x = quiet_zone_mm

    for bit in pattern:

        if bit == "1":

            SubElement(
                svg,
                "rect",
                x=str(x * MM_TO_PX),
                y="0",
                width=str(module_width * MM_TO_PX),
                height=str(height_mm * MM_TO_PX),
                fill="black"
            )

        x += module_width

    ElementTree(svg).write(
        filename,
        encoding="utf-8",
        xml_declaration=True
    )