from load_image import ft_load
from matplotlib.pyplot import imshow, show, close, gcf


def close_figure(event):
    if event.key == 'q':
        close(event.canvas.figure)


def ft_transpose(path):
    """ft_transpose change direction of the image"""
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
    transposed = [[zoom_arr[y][x] for y in range(new_h)] for x in range(new_l)]
    print(f"New shape after Transpose: {zoom_arr.shape}")
    imshow(transposed, cmap='gray')
    fig = gcf()  # allow me to setup event key
    fig.canvas.mpl_connect('key_press_event', close_figure)  # setup event key
    show()
    print(transposed)


def main():
    try:
        ft_transpose("./images/animal.jpeg")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == "__main__":
    main()
