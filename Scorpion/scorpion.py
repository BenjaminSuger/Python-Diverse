#!/usr/bin/env python3

from sys import argv
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def format(value) -> str:
    """Return a printable version of value, truncated if it is too big"""
    MAX_LEN = 100
    if isinstance(value, bytes) and len(value) > MAX_LEN:
        return f"bytes; {len(value)} octets"
    if isinstance(value, str) and len(value) > MAX_LEN:
        return value[:MAX_LEN] + f"...(+{len(value) - MAX_LEN} caracteres)"
    return str(value)


def print_dict(data: dict, names: dict = TAGS) -> None:
    """print the dict with the right name"""
    for tag_id, value in data.items():
        tag_name = names.get(tag_id, tag_id)
        print(f"{tag_name} ({tag_id}): {format(value)}")


def scorpion(argv: list) -> None:
    """Show EXIF data for images"""
    if len(argv) < 2:
        print("Not enough arguments\nUsage: ./scorpion FILE1 [FILE2 ...]")
        return
    for i in range(1, len(argv)):
        print(40 * '-')
        print(f"NAME: {argv[i]}\n")
        try:
            img = Image.open(argv[i])
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            continue

        img_exif = img.getexif()
        if not img_exif:
            print("No EXIF data")
        else:
            print("EXIF:")
            print_dict(img_exif)

        gps_ifd  = img_exif.get_ifd(0x8825)
        if not gps_ifd:
            print("No GPS data")
        else:
            print("\nGPS DATA:")
            print_dict(gps_ifd, GPSTAGS)


        exif_ifd = img_exif.get_ifd(0x8769)
        if not exif_ifd:
            print("No more data")
        else:
            print("\nSUB EXIF:")
            print_dict(exif_ifd)


if __name__ == "__main__":
    scorpion(argv)
