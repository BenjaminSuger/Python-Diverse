import numpy
from PIL import Image
import matplotlib.pyplot as plt #la j'aurais peut etre pas besoin pour cette exo mais pour les prochains

#faudra bien tester aussi une image "vide"

def ft_load(path: str) -> array: #je peux changer l'output
    """Load JPG or JPEG and print information about the img"""
    img = Image.open(path)
    print(img.load()) 



if __name__ == "__main__":
    try:
        print(ft_load("./images/animal.jpeg"))
        print(ft_load("tester.py"))
    except Exception as e:
        print(f"{type(e).__name__} : {e}")
