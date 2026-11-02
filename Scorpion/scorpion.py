#!/usr/bin/env python3

from sys import argv
from PIL import Image, ExifTags

def scorpion(argv: list) -> None:
    if len(argv) < 2:
        print("Not enough arguments\nUsage: ./scorpion FILE1 [FILE2 ...]")
        return
    for i in range(1, len(argv)):
        print(argv[i])
        img = Image.open(argv[i])
        img_exif = img.getexif()
        print(img_exif)


if __name__ == "__main__":
    scorpion(argv)
