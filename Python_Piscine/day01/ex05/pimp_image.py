from load_image import ft_load
from matplotlib.pyplot import imshow, show, close, gcf


def close_figure(event) -> None:
    """function to close the image with the q key"""
    if event.key == 'q':
        close(event.canvas.figure)


def show_img(img: list) -> None:
    """function to print the img from a list"""
    imshow(img, cmap='gray')
    fig = gcf()
    fig.canvas.mpl_connect('key_press_event', close_figure)
    show()


def ft_invert(array) -> list:
    """Inverts the color of the image received."""
    array = 255 - array
    show_img(array)


def ft_red(array) -> list:
    """redify the image received"""
    array = [1, 0, 0] * array
    show_img(array)


def ft_green(array) -> list:
    """green like the lantern the image received."""
    new_array = array.copy()
    new_array[:, :, 0] -= new_array[:, :, 0]
    new_array[:, :, 2] -= new_array[:, :, 2]
    show_img(new_array)


def ft_blue(array) -> list:
    """blue da ba dee da the image received"""
    new_array = array.copy()
    new_array[:, :, 0] = 0
    new_array[:, :, 1] = 0
    show_img(new_array)


def ft_grey(array) -> list:
    """Grey the image received"""
    new_array = array.copy()
    new_array[:, :, 0] = new_array[:, :, 1]
    new_array[:, :, 2] = new_array[:, :, 1]
    show_img(new_array)


def main():
    try:
        array = ft_load("./images/landscape.jpg")
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == "__main__":
    main()
