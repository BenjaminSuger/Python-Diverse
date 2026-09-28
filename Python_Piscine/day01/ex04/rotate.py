from load_image import ft_load
from matplotlib.pyplot import imshow, show, close, gcf


def close_figure(event) -> None:
    """function to close the image with the q key"""
    if event.key == 'q':
        close(event.canvas.figure)


def show_img(transposed: list) -> None:
    """function to print the img from a list"""
    imshow(transposed, cmap='gray')
    fig = gcf()
    fig.canvas.mpl_connect('key_press_event', close_figure)
    show()


def preparation_img(path: str) -> (list, int, int):
    """make the zoom for the img and print the shape
    return the new img as a list and new height and
    the new length (in this order)"""
    arr = ft_load(path)
    height, length = arr.shape[0], arr.shape[1]
    new_h = height // 2
    new_l = length // 2
    centre_y = height // 2
    centre_x = length // 2
    new_y = centre_y - new_h // 2
    new_x = centre_x - new_l // 2
    zoom_arr = arr[new_y:new_y + new_h, new_x:new_x + new_l, 0]
    zoom_arr3d = arr[new_y:new_y + new_h, new_x:new_x + new_l, 0:1]
    print(f"The shape of image is : {zoom_arr3d.shape} or {zoom_arr.shape}")
    print(zoom_arr3d)
    return zoom_arr, new_h, new_l


def ft_transpose(path: str) -> None:
    """ft_transpose change direction of the image"""
    zoom_arr, new_h, new_l = preparation_img(path)
    trp = [[int(zoom_arr[y][x]) for y in range(new_h)] for x in range(new_l)]
    print(f"New shape after Transpose: {zoom_arr.shape}")
    show_img(trp)
    print(trp)


def main():
    try:
        ft_transpose("./images/animal.jpeg")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == "__main__":
    main()
