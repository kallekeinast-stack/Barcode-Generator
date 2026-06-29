from engine.generator import BarcodeGenerator


generator = BarcodeGenerator()

generator.generate(
    year=2026,
    start=1,
    end=20
)