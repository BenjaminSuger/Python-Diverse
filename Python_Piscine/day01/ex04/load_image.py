from numpy import asarray
from PIL import Image


def ft_load(path: str) -> list:
    """Load JPG or JPEG and print information about the img"""
    img = Image.open(path)
    if img.format != "JPEG":
        raise TypeError("Image is not a JPEG or JPG")
    result = asarray(img)
    # print(f"The shape of image is : {result.shape}")
    return result


if __name__ == "__main__":
    try:
        print(ft_load("./images/landscape.jpg"))
    except Exception as e:
        print(f"{type(e).__name__} : {e}")
