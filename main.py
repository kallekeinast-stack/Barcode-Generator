from pathlib import Path

from config import settings


def main():

    print("=" * 40)
    print("Barcode Generator")
    print("=" * 40)

    print(f"Aasta      : {settings.YEAR}")
    print(f"Algus      : {settings.START}")
    print(f"Lõpp       : {settings.END}")

    print(f"Laius      : {settings.WIDTH_MM} mm")
    print(f"Kõrgus     : {settings.HEIGHT_MM} mm")

    Path(settings.OUTPUT_FOLDER).mkdir(exist_ok=True)

    print("\nValmis.")


if __name__ == "__main__":
    main()