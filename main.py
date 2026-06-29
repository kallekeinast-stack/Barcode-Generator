from pathlib import Path


def main():
    print("=" * 40)
    print("Barcode Generator")
    print("Version 0.1")
    print("=" * 40)

    Path("output").mkdir(exist_ok=True)
    Path("input").mkdir(exist_ok=True)

    print("Projekt on valmis.")


if __name__ == "__main__":
    main()
