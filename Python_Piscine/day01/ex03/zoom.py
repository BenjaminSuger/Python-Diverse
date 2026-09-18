from load_image import ft_load
import matplotlib.pyplot as plt #temporaire parce que pas legit


def ft_zoom(path: str, zoom: int ) -> list:
    # a mon avis des securite sur le zoom
    # mais je sasi pas comment faire le zoom
    arr = ft_load(path)
    print(arr)


if __name__ == "__main__":
    try:
        ft_zoom("./images/animal.jpeg")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")
